# Generated by Django 5.0.6 on 2024-11-28 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0011_flare_remove_dayflarelist_year_month_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="flarelist",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2024, 11, 28, 6, 57, 43, 970855),
            ),
            preserve_default=False,
        ),
    ]
