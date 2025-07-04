# Generated by Django 5.0.6 on 2024-11-20 16:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminLevel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_type', models.CharField(choices=[('INCOME', 'Income Tax'), ('PROPERTY', 'Property Tax')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('OVERDUE', 'Overdue')], default='PENDING', max_length=20)),
                ('due_date', models.DateField()),
                ('payment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxPayerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIN', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^\\+?\\d{10,15}$')])),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('kebele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='AdminLevel.kebele')),
            ],
        ),
    ]
