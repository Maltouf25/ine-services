# Generated by Django 4.1.7 on 2023-04-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reclamation", "0007_reclamation_time"),
    ]

    operations = [
        migrations.RemoveField(model_name="reclamation", name="time",),
    ]
