from rest_framework import serializers
from .models import TaxPayerProfile
class TaxPayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxPayerProfile
        fields = ['TIN', 'address', 'phone_number', 'bio', 'avatar', 'kebele']