# Generated by Django 4.1.7 on 2023-04-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reclamation", "0009_reclamation_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="reclamation",
            name="terminer",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reclamation",
            name="traitement",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
