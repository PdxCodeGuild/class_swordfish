from django.db import models

# Create your models here.
# First Name (CharField)
# Last Name (CharField)
# Cohort (CharField)
# Favorite Topic (CharField)
# Favorite Teacher (CharField)
# Capstone (URLField)

class Student(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        cohort = models.CharField(max_length=30)
        favorite_topic = models.CharField(max_length=30, null=True, blank=True)
        favorite_teacher = models.CharField(max_length=30, null=True, blank=True)
        capstone = models.URLField(max_length=200, null=True, blank=True)

        def __str__(self):
            return self.first_name + " " + self.last_name