# Generated by Django 4.1.3 on 2022-12-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_posts_post_author_posts_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
