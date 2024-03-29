# Generated by Django 5.0.1 on 2024-01-12 06:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chatroom_is_group_chat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ManyToManyField(blank=True, related_name='recipient', to=settings.AUTH_USER_MODEL),
        ),
    ]
