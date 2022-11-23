from django.db import models

class StudentList(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cohort = models.CharField(max_length=20, null=True, blank=True)
    favorite_topic = models.CharField(max_length=20, null=True, blank=True)
    favorite_teacher = models.CharField(max_length=20, null=True, blank=True)
    capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name