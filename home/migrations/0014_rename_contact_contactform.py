# Generated by Django 4.1.3 on 2022-11-08 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_contact"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="contact",
            new_name="ContactForm",
        ),
    ]