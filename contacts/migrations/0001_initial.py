# Generated by Django 4.0.2 on 2022-02-14 02:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(message='Invalid phone number. Must include country code and DDD.', regex='^[0-9]{2} [0-9]{1,2} [0-9]{9}')])),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.EmailValidator(message='Invalid email address.')])),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.category')),
            ],
        ),
    ]
