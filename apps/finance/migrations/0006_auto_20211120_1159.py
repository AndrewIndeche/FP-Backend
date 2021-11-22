# Generated by Django 3.2.9 on 2021-11-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20211120_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='approved_expenses',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='status',
        ),
        migrations.RemoveField(
            model_name='expenses',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='expenses',
            name='merchant',
            field=models.CharField(default='', max_length=100),
        ),
    ]
