# Generated by Django 3.2.9 on 2021-12-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0005_feeqr'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary01',
            name='CBQAMOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary01',
            name='CBQCOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary01',
            name='CBQFEE',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary02',
            name='CBQAMOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary02',
            name='CBQCOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary02',
            name='CBQFEE',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary03',
            name='CBQAMOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary03',
            name='CBQCOUNT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='summary03',
            name='CBQFEE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]