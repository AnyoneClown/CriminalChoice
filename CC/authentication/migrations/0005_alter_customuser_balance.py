# Generated by Django 4.1 on 2023-08-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_customuser_balance_alter_customuser_rank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
    ]