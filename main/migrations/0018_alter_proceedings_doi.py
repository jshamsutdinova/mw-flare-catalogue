# Generated by Django 5.0.6 on 2024-11-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_conference_website_alter_proceedings_doi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proceedings",
            name="doi",
            field=models.URLField(blank=True, null=True),
        ),
    ]
