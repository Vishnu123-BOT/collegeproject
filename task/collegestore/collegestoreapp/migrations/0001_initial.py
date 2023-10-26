# Generated by Django 4.1 on 2023-10-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="Department")),
            ],
        ),
    ]
