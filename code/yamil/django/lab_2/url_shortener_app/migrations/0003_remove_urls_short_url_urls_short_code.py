# Generated by Django 4.1.3 on 2022-11-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0002_rename_test_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='short_url',
        ),
        migrations.AddField(
            model_name='urls',
            name='short_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
