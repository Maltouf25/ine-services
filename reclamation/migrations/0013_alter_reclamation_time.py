# Generated by Django 4.1.7 on 2023-04-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reclamation", "0012_alter_reclamation_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reclamation", name="time", field=models.DateTimeField(),
        ),
    ]
