# Generated by Django 4.1.3 on 2022-11-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=50)),
                ('cohort', models.CharField(max_length=50)),
                ('favorite_topic', models.CharField(max_length=50)),
                ('favorite_teacher', models.CharField(max_length=50)),
                ('capstone', models.URLField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]