# Generated by Django 4.1.3 on 2022-12-08 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chirp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiny_body', models.CharField(max_length=127)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chirps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
