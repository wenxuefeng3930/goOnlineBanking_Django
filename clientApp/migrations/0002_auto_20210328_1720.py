# Generated by Django 3.1.7 on 2021-03-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
