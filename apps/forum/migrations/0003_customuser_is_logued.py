# Generated by Django 4.2.2 on 2023-08-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_customuser_registration_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_logued',
            field=models.BooleanField(default=False),
        ),
    ]
