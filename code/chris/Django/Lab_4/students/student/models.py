from django.db import models

# Create student Model to represent data

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
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=30)
    capstone = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.last_name + ", " + self.first_name