# Generated by Django 5.0.6 on 2024-06-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_users_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]