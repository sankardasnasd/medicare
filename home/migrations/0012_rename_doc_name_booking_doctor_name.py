# Generated by Django 4.1.3 on 2022-11-08 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_rename_dep_name_doctors_department_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="doc_name",
            new_name="doctor_name",
        ),
    ]