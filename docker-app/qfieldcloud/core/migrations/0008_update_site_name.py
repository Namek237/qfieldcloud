# Generated by Django 2.2.17 on 2020-12-31 15:04

from django.conf import settings
from django.db import migrations


def update_site_name(apps, schema_editor):
    site_model = apps.get_model("sites", "Site")
    domain = "qfield.cloud"
    name = "QFieldCloud"

    site_model.objects.update_or_create(
        pk=settings.SITE_ID, defaults={"domain": domain, "name": name}
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_project_overwrite_conflicts"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]