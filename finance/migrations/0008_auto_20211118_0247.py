# Generated by Django 3.2.9 on 2021-11-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20211118_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='employee_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='insurance_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='tax_pin_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='work_email',
            field=models.CharField(max_length=100),
        ),
    ]
