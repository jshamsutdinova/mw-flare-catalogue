# Generated by Django 5.0.6 on 2024-12-02 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0019_alter_flarelist_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flarelist",
            name="date",
            field=models.DateField(unique=True),
        ),
    ]