from django.db import models
from accounts.models import User
from django.utils import timezone
from datetime import timedelta
from AdminLevel.models import Kebele
from django.core.validators import RegexValidator
class TaxPayerProfile(models.Model):
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
      TIN=models.CharField(max_length=50,unique=True)
      address=models.TextField()
      phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?\d{10,15}$', message='Enter a valid phone number')])      
      registered_at=models.DateTimeField(auto_now_add=True)
      kebele = models.ForeignKey(Kebele, on_delete=models.CASCADE, related_name="users")
      bio = models.TextField(blank=True, null=True)  # Optional bio field (text)
      avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
      def __str__(self):
        return f"{self.user.username} - {self.TIN}"
      def get_full_address(self):
        return f"{self.address}, Kebele: {self.kebele.name if self.kebele else 'N/A'}"
      def is_registered_recently(self):
        return self.registered_at >= timezone.now() - timedelta(days=30)


class TaxRecord(models.Model):
      TAX_TYPE_CHOICE=[
            ('INCOME','Income Tax'),
            ('PROPERTY', 'Property Tax'),
      ]
      STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'Overdue'),
       ]
      
      taxpayer=models.ForeignKey('TaxPayerProfile',on_delete=models.CASCADE,related_name="tax_records")
      tax_type=models.CharField(max_length=20,choices=TAX_TYPE_CHOICE)
      amount=models.DecimalField(max_digits=10,decimal_places=2)
      status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
      due_date=models.DateField()
      payment_date=models.DateField(null=True,blank=True)
      


