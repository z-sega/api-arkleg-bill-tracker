# Generated by Django 4.2.18 on 2025-01-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bill", "0002_bill_legiscan_bill_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="bill",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
