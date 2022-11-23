from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=50)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=50)
    capstone = models.URLField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    