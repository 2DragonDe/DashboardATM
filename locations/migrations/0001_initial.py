# Generated by Django 3.1.4 on 2021-01-14 01:32

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.city')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.district')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('setup', models.CharField(choices=[('xp', 'XP'), ('xt', 'XT'), ('s', 'S')], max_length=10)),
                ('area', models.CharField(choices=[('in', '??i???m Trong ACB'), ('out', '??i???m Ngo??i ACB')], max_length=20)),
                ('contact01', models.CharField(max_length=100)),
                ('contact02', models.CharField(max_length=100)),
                ('contact03', models.CharField(max_length=100)),
                ('contact04', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.city')),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='city', chained_model_field='city', limit_choices_to={'name__startswith': 'H'}, on_delete=django.db.models.deletion.CASCADE, to='locations.district')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.manager')),
                ('ward', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='district', chained_model_field='district', limit_choices_to={'name__startswith': 'H'}, on_delete=django.db.models.deletion.CASCADE, to='locations.ward')),
            ],
        ),
    ]
