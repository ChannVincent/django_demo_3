# Generated by Django 4.0.6 on 2022-08-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_app', '0004_remove_share_count_enterprise_share_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('background', models.CharField(default='', max_length=200)),
                ('enterprises', models.ManyToManyField(to='financial_app.enterprise')),
            ],
        ),
    ]
