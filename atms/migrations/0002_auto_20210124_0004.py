# Generated by Django 3.1.4 on 2021-01-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='camera_ip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='atm',
            name='gateway',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='atm',
            name='ip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
