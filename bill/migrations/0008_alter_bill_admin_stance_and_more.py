# Generated by Django 4.2.19 on 2025-02-14 22:27

from django.db import migrations, models


def forward_change_approve_to_support(apps, schema_editor):
    """Change "approve" to "support"."""

    UserBillInteraction = apps.get_model("bill", "UserBillInteraction")
    Bill = apps.get_model("bill", "Bill")

    UserBillInteraction.objects.filter(stance="approve").update(stance="support")
    Bill.objects.filter(admin_stance="approve").update(admin_stance="support")


def reverse_change_support_to_approve(apps, schema_editor):
    """Change "support" back to "approve"."""

    UserBillInteraction = apps.get_model("bill", "UserBillInteraction")
    Bill = apps.get_model("bill", "Bill")

    UserBillInteraction.objects.filter(stance="support").update(stance="approve")
    Bill.objects.filter(admin_stance="support").update(admin_stance="approve")


class Migration(migrations.Migration):

    dependencies = [
        ("bill", "0007_tag_alter_userbillinteraction_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="admin_stance",
            field=models.CharField(
                blank=True,
                choices=[
                    ("support", "Support"),
                    ("oppose", "Oppose"),
                    ("watch", "Watch"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userbillinteraction",
            name="stance",
            field=models.CharField(
                blank=True,
                choices=[
                    ("support", "Support"),
                    ("oppose", "Oppose"),
                    ("watch", "Watch"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.RunPython(
            forward_change_approve_to_support, reverse_change_support_to_approve
        ),
    ]
