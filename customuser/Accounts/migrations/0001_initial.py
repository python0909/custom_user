# Generated by Django 3.2.6 on 2021-08-11 12:37

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(blank=True, default='user', max_length=20)),
                ('email', models.EmailField(error_messages={'unique': 'This email has already been registered.'}, max_length=40, unique=True)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=13, region='IN')),
                ('address', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
