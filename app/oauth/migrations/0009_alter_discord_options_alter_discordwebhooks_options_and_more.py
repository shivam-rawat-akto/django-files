# Generated by Django 4.2.4 on 2023-09-07 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth.models


class Migration(migrations.Migration):
    dependencies = [
        ("oauth", "0008_discordwebhooks"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="discord",
            options={"verbose_name": "Discord", "verbose_name_plural": "Discords"},
        ),
        migrations.AlterModelOptions(
            name="discordwebhooks",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Discord Webhook",
                "verbose_name_plural": "Discord Webhooks",
            },
        ),
        migrations.AlterModelOptions(
            name="github",
            options={"verbose_name": "Github", "verbose_name_plural": "Githubs"},
        ),
        migrations.CreateModel(
            name="UserInvites",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "invite",
                    models.CharField(default=oauth.models.rand_invite, max_length=16),
                ),
                (
                    "expire",
                    models.IntegerField(
                        default=0,
                        help_text="Expiration Seconds.",
                        verbose_name="Expire",
                    ),
                ),
                (
                    "max_uses",
                    models.IntegerField(
                        default=1, help_text="Max Uses.", verbose_name="Max"
                    ),
                ),
                (
                    "uses",
                    models.IntegerField(
                        default=0, help_text="Total Uses.", verbose_name="Uses"
                    ),
                ),
                (
                    "user_ids",
                    models.JSONField(
                        default=list,
                        help_text="Users who Used Invite.",
                        verbose_name="User IDs",
                    ),
                ),
                (
                    "super_user",
                    models.BooleanField(
                        default=False,
                        help_text="Invited Users are Super Users.",
                        verbose_name="Super",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Invite Created Date.",
                        verbose_name="Created",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Invite Updated Date.",
                        verbose_name="Updated",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Invite",
                "verbose_name_plural": "User Invites",
                "ordering": ["-created_at"],
            },
        ),
    ]
