# Generated by Django 4.1.2 on 2022-10-21 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "grocery",
            "0002_groceryitem_completed_date_groceryitem_created_date_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="groceryitem", old_name="grocery_item", new_name="description",
        ),
    ]