# Generated by Django 3.2.7 on 2021-10-01 22:01

import django.db.models.deletion
import qfieldcloud.authentication.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        db_index=True,
                        default=qfieldcloud.authentication.models.generate_token_key,
                        max_length=300,
                        unique=True,
                        verbose_name="Token",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "expires_at",
                    models.DateTimeField(
                        default=qfieldcloud.authentication.models.generate_token_expires_at,
                        verbose_name="Expires at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "last_used_at",
                    models.DateTimeField(null=True, verbose_name="Last used at"),
                ),
                ("user_agent", models.TextField(blank=True, verbose_name="User-Agent")),
                (
                    "client_type",
                    models.CharField(
                        choices=[
                            ("browser", "Browser"),
                            ("cli", "Command line interface"),
                            ("sdk", "SDK"),
                            ("qfield", "QField"),
                            ("qfieldsync", "QFieldSync"),
                            ("unknown", "Unknown"),
                        ],
                        default="unknown",
                        max_length=32,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_tokens",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Token",
                "verbose_name_plural": "Tokens",
                "ordering": ("-created_at",),
            },
        ),
    ]
