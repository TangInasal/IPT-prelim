# Generated by Django 5.1.5 on 2025-02-13 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
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
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("sedan", "Sedan"),
                            ("suv", "SUV"),
                            ("luxury", "Luxury"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "transmission",
                    models.CharField(
                        choices=[("automatic", "Automatic"), ("manual", "Manual")],
                        max_length=50,
                    ),
                ),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("petrol", "Petrol"),
                            ("diesel", "Diesel"),
                            ("electric", "Electric"),
                        ],
                        max_length=50,
                    ),
                ),
                ("location", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("gps", models.BooleanField(default=False)),
                ("child_seats", models.BooleanField(default=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("availability", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "vehicle",
            },
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("loyalty_points", models.FloatField(default=0.0)),
                ("country", models.CharField(default="Philippines", max_length=100)),
                ("language", models.CharField(default="English", max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "customer",
            },
        ),
        migrations.CreateModel(
            name="Review",
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
                ("comment", models.TextField()),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "1 - Poor"),
                            (2, "2 - Fair"),
                            (3, "3 - Good"),
                            (4, "4 - Very Good"),
                            (5, "5 - Excellent"),
                        ]
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="citydrive.customer",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="citydrive.vehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Review",
                "verbose_name_plural": "Reviews",
                "db_table": "review",
                "ordering": ["rating"],
            },
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("pickup_location", models.CharField(max_length=200)),
                ("dropoff_location", models.CharField(max_length=200)),
                ("pickup_date", models.DateField()),
                ("dropoff_date", models.DateField()),
                (
                    "payment_type",
                    models.CharField(
                        choices=[
                            ("credit_card", "Credit Card"),
                            ("debit_card", "Debit Card"),
                            ("digital_wallet", "Digital Wallet"),
                        ],
                        max_length=50,
                    ),
                ),
                ("payment_status", models.BooleanField(default=False)),
                (
                    "booking_status",
                    models.CharField(
                        choices=[("successful", "Successful"), ("failed", "Failed")],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="citydrive.vehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Booking",
                "verbose_name_plural": "Bookings",
                "db_table": "booking",
                "ordering": ["payment_status", "pickup_date"],
                "unique_together": {("user", "vehicle", "pickup_date")},
            },
        ),
    ]
