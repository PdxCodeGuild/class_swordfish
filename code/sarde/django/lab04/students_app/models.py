from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cohort = models.CharField(max_length=20)
    favorite_topic = models.CharField(max_length=20)
    favorite_teacher = models.CharField(max_length=20)
    capstone = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name
