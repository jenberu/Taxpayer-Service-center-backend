from rest_framework import serializers
from accounts.models import User
class UserSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(source='public_id',read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    class Meta:
       model = User
       fields = ['id', 'username', 'first_name',
                'last_name', 'bio', 'avatar', 'email',
                'is_active', 'created', 'updated']
       read_only_fields = ['is_active']
class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128,min_length=8, write_only=True, required=True)
    class Meta:
        model=User
        fields = ['id', 'bio', 'avatar', 'email',
                'username', 'first_name', 'last_name',
                'password']
    def create(self, validated_data):#This method is called when the serializer.save() method is executed 
        # `validated_data` contains the validated input data for fields in the serializer
    # For example: {'username': 'john_doe', 'email': 'john@example.com', 'password': 'securepassword'}
 # Use the `create_user` method we wrote earlier for the UserManager to create a new user.
      return User.objects.create_user(**validated_data)    

