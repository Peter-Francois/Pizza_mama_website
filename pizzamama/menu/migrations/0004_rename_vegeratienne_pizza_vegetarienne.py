# Generated by Django 5.1.1 on 2024-10-04 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_pizzas_pizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='vegeratienne',
            new_name='vegetarienne',
        ),
    ]
