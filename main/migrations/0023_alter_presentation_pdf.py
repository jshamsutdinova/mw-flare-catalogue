# Generated by Django 5.0.6 on 2025-01-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0022_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="presentation",
            name="pdf",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
