# Generated by Django 5.1.5 on 2025-02-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("citydrive", "0002_alter_booking_booking_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_status",
            field=models.CharField(
                choices=[("failed", "Failed"), ("successful", "Successful")],
                max_length=50,
            ),
        ),
    ]
