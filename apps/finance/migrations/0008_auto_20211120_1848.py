# Generated by Django 3.2.9 on 2021-11-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_alter_expenses_merchant'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='approved_expenses',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='expenses',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=40),
        ),
        migrations.AddField(
            model_name='payroll',
            name='hours',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='purposes',
            field=models.CharField(default='', max_length=30),
        ),
    ]