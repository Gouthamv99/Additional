# Generated by Django 5.0.3 on 2024-04-11 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_eventimage_event_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='image',
        ),
    ]
