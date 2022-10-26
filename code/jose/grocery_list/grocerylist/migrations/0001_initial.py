# Generated by Django 4.1.2 on 2022-10-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('completed_item', models.BooleanField(default=False)),
                ('grocery_list', models.CharField(max_length=100)),
            ],
        ),
    ]
