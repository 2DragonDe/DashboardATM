# Generated by Django 3.2.9 on 2021-12-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0004_summaryatm'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeQR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_id', models.CharField(blank=True, max_length=10, null=True)),
                ('fee_qr', models.IntegerField(default=0)),
            ],
        ),
    ]
