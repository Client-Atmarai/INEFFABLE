# Generated by Django 4.2.3 on 2023-07-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ineffable_app", "0025_delete_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status_create",
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
                ("status", models.CharField(max_length=30)),
                ("student_rollno", models.IntegerField()),
            ],
        ),
    ]