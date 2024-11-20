from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets,views
from .serializers import UserSerializer
from .models import User
from django.http import Http404
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.exceptions import InvalidToken,TokenError
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.decorators import api_view,permission_classes
# from django.contrib.auth.models import AnonymousUser
from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 10 
class UserViewSet(viewsets.ModelViewSet):
    http_method_names=('patch','get')
    permission_classes=[AllowAny]
    serializer_class=UserSerializer
    pagination_class=CustomPagination

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    def get_object(self):
        try:
            obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
            return obj
        except Http404:
            raise Http404("User with this public ID does not exist.")
class RegisterViewSet(viewsets.ViewSet):
     serializer_class = RegisterSerializer
     permission_classes=[AllowAny]
     http_method_names=['post']
     #create method is called when the view is accessed via a POST request.
     def create(self,request,*args,**kwargs):
         try:
            serializer=self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            #riggers the create method defined in the RegisterSerializer
            user=serializer.save()
            #reates a new refresh token associated with the user
            refresh=RefreshToken.for_user(user)
            response_data = {
                    "user": serializer.data,
                    "refresh": str(refresh),
                    "token": str(refresh.access_token)
                }
            return Response(response_data, status=status.HTTP_201_CREATED)
         except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        serializer =self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:

            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data,status=status.HTTP_200_OK)   

class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data,status=status.HTTP_200_OK)
@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response({'user': serializer.data})


class LogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)  # Add a comma to make it a tuple
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")  
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
