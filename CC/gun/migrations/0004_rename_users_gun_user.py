# Generated by Django 4.1 on 2023-08-21 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gun', '0003_remove_gun_user_gun_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gun',
            old_name='users',
            new_name='user',
        ),
    ]
