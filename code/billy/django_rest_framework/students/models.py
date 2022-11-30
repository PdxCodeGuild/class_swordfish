from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cohort = models.CharField(max_length=30)
    favorite_topic = models.CharField(max_length=30)
    favorite_teacher = models.CharField(max_length=30)
    capstone = models.URLField(max_length=2083,null=True, blank=True)

    def __str__(self):
        return self.first_name