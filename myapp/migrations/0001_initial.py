# Generated by Django 3.2.6 on 2021-08-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.CharField(max_length=100)),
                ('expertise', models.CharField(max_length=100)),
            ],
        ),
    ]