# Generated by Django 4.1.3 on 2022-11-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='completed',
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='list_text',
            field=models.CharField(default='Item', max_length=200),
        ),
    ]
