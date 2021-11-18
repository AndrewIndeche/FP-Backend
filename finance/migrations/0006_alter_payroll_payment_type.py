# Generated by Django 3.2.9 on 2021-11-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_payroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='payment_type',
            field=models.CharField(choices=[('MOBILE', 'mobile'), ('BANK', 'bank account')], default='', max_length=20),
        ),
    ]
