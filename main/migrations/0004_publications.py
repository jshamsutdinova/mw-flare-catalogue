# Generated by Django 5.0.6 on 2024-06-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_team_email_alter_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.TextField()),
                ('title', models.TextField()),
                ('journal', models.TextField()),
                ('doi', models.CharField(max_length=20)),
            ],
        ),
    ]
