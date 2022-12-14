# Generated by Django 4.1.2 on 2022-10-21 17:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("grocery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="groceryitem",
            name="completed_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="groceryitem",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="groceryitem",
            name="task_completed",
            field=models.BooleanField(default=False),
        ),
    ]
