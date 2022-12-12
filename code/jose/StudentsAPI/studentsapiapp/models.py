from django.db import models

# Create your models here.
class Students(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Cohort = models.CharField(max_length=50)
    Favorite_topic = models.CharField(max_length=50)
    Favorite_teacher = models.CharField(max_length=50)
    Capstone = models.CharField(max_length=50, null= True)

    def __str__ (self):
        return self.Last_name

    class Meta:
        ordering = ['-Last_name']
