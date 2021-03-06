# Generated by Django 3.2.9 on 2021-11-15 11:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('rather_not_say', 'rather_not_say')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='KE'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='personal email'),
        ),
    ]
