# Generated by Django 4.0 on 2022-07-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='bio',
            field=models.TextField(blank=True, default='i am a new user', null=True),
        ),
    ]
