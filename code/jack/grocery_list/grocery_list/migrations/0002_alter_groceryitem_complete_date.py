# Generated by Django 4.1.2 on 2022-10-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='complete_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
