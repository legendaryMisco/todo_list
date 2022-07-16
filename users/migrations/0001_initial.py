# Generated by Django 4.0 on 2022-07-15 12:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('phonenumber', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=400, null=True)),
                ('profile_image', models.ImageField(blank=True, default='user-default.png', max_length=3000, null=True, upload_to='profile_image/')),
                ('short_intro', models.CharField(blank=True, default='i am a new user', max_length=300, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[['boy', 'MALE'], ['girl', 'FEMALE']], max_length=10, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
