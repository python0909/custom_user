# Generated by Django 3.2.6 on 2021-08-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
