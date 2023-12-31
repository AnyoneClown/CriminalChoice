# Generated by Django 4.1 on 2023-08-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'Visitor'), (1, 'Mafia'), (2, 'Gang'), (3, 'Admin')], default=0),
        ),
    ]
