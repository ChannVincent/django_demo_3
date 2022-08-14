# Generated by Django 4.0.6 on 2022-08-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_app', '0002_enterprise_logo_url_enterprise_sector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dividend',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='share',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
