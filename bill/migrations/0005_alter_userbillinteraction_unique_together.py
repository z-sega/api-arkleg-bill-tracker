# Generated by Django 4.2.18 on 2025-01-31 18:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bill", "0004_rename_title_bill_bill_title"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userbillinteraction",
            unique_together={("user", "bill")},
        ),
    ]
