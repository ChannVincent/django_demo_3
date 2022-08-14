# Generated by Django 4.0.6 on 2022-08-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-name', '-ticker'],
            },
        ),
    ]
