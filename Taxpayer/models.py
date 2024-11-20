from django.db import models
from accounts.models import User
class TaxPayerProfile(models.Model):
      user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile'),
      TIN=models.CharField(max_length=50,unique=True)
      address=models.TextField()
      phone_number=models.CharField(max_length=15)
      reisterd_at=models.DateTimeField(auto_now_add=True)

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
      
      taxpayer=models.ForeignKey(TaxPayerProfile,on_delete=models.CASCADE,related_name="tax_records")
      tax_type=models.CharField(max_length=20,choices=TAX_TYPE_CHOICE)
      amount=models.DecimalField(max_digits=10,decimal_places=2)
      status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
      due_date=models.DateField()
      payment_date=models.DateField(null=True,blank=True)
      


