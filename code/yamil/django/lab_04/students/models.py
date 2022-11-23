from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cohort = models.CharField(max_length=50)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=20)
    capstone = models.URLField(max_length=100)

    def __str__(self):
        return (self.first_name)
