# Generated by Django 4.1.3 on 2022-12-02 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_title',
            new_name='post_author',
        ),
    ]
