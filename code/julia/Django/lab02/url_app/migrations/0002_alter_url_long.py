# Generated by Django 4.1.3 on 2022-12-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long',
            field=models.TextField(max_length=200),
        ),
    ]
