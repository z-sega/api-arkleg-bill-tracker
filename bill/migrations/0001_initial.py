# Generated by Django 4.2.18 on 2025-01-30 00:21

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bill",
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
                    "bill_number",
                    models.CharField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "admin_stance",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Approve"),
                            ("oppose", "Oppose"),
                            ("watch", "Watch"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("admin_note", models.TextField(blank=True, null=True)),
                ("admin_expanded_analysis_url", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserKeyword",
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
                ("keyword", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="keywords",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserBillInteraction",
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
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("note", models.TextField(blank=True, null=True)),
                (
                    "stance",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("approve", "Approve"),
                            ("oppose", "Oppose"),
                            ("watch", "Watch"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "bill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interactions",
                        to="bill.bill",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bill_interactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
