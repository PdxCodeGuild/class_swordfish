# Generated by Django 4.1.3 on 2022-12-05 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='updated',
        ),
    ]
