# Generated by Django 5.0.6 on 2024-11-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_alter_proceedings_options_alter_proceedings_journal"),
    ]

    operations = [
        migrations.AddField(
            model_name="conference",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="proceedings",
            name="doi",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="publication",
            name="doi",
            field=models.CharField(max_length=50),
        ),
    ]
