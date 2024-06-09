# Generated by Django 3.2.13 on 2022-05-05 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0052_secret"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="secret",
            options={"ordering": ["project", "name"]},
        ),
        migrations.AlterField(
            model_name="secret",
            name="name",
            field=models.TextField(
                help_text="Must start with a capital letter and followed by capital letters, numbers or underscores.",
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Z]+[A-Z0-9_]+$",
                        "Must start with a capital letter and followed by capital letters, numbers or underscores.",
                    )
                ],
            ),
        ),
        migrations.AddConstraint(
            model_name="secret",
            constraint=models.UniqueConstraint(
                fields=("project", "name"), name="secret_project_name_uniq"
            ),
        ),
    ]
