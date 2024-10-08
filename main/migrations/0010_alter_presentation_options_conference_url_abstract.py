# Generated by Django 5.0.6 on 2024-07-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_presentation_id_conf_presentation_conf_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presentation',
            options={'ordering': ['-type', 'name']},
        ),
        migrations.AddField(
            model_name='conference',
            name='url_abstract',
            field=models.URLField(null=True),
        ),
    ]
