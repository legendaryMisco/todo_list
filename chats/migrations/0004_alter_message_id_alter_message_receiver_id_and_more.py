# Generated by Django 4.0 on 2022-07-15 23:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_register_bio'),
        ('chats', '0003_alter_message_id_alter_message_receiver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a88c3027-409c-4fda-ade8-fd998c225162'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.register'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fb8cd541-b02a-462a-aa21-5996af187816'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
