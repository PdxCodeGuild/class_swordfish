from django.db import models

# Create your models here.
# title
# description (optional)
# completed
# created_at

class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=128, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
