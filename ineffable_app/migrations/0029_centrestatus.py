# Generated by Django 4.2.3 on 2023-07-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ineffable_app", "0028_status_create"),
    ]

    operations = [
        migrations.CreateModel(
            name="CentreStatus",
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
                ("centrecode", models.IntegerField()),
                ("centreowner", models.CharField(max_length=30)),
                ("centrename", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=100)),
                ("mob", models.IntegerField()),
                ("centre_status", models.CharField(max_length=10)),
                ("centreimage", models.ImageField(upload_to="")),
            ],
        ),
    ]