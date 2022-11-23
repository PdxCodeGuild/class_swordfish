# Generated by Django 4.1.3 on 2022-11-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('cohort', models.CharField(blank=True, max_length=20, null=True)),
                ('favorite_topic', models.CharField(blank=True, max_length=20, null=True)),
                ('favorite_teacher', models.CharField(blank=True, max_length=20, null=True)),
                ('capstone', models.URLField()),
            ],
        ),
    ]
