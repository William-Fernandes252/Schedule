# Generated by Django 4.0.2 on 2022-02-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='surname',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
