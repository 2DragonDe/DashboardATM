# Generated by Django 3.1.4 on 2021-01-14 02:00

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='district',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='city', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='locations.district'),
        ),
        migrations.AlterField(
            model_name='location',
            name='ward',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', on_delete=django.db.models.deletion.CASCADE, to='locations.ward'),
        ),
    ]
