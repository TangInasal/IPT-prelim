# Generated by Django 5.1.5 on 2025-02-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("citydrive", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_status",
            field=models.CharField(
                choices=[("paid", "Paid"), ("pending", "Pending")], max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="payment_type",
            field=models.CharField(
                choices=[
                    ("credit_card", "Credit Card"),
                    ("debit_card", "Debit Card"),
                    ("cash", "CASH"),
                    ("digital_wallet", "Digital Wallet"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                choices=[(1, "1"), (2, "2 "), (3, "3"), (4, "4 "), (5, "5 ")]
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="fuel_type",
            field=models.CharField(
                choices=[("petrol", "Petrol"), ("diesel", "Diesel")], max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="vehicle_type",
            field=models.CharField(
                choices=[
                    ("sedan", "Sedan"),
                    ("suv", "SUV"),
                    ("pick up", "Pick up"),
                    ("mpv", "MPV"),
                    ("wing van", "Wing Van"),
                    ("van", "VAN"),
                ],
                max_length=50,
            ),
        ),
    ]
