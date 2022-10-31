from django.db import models
from django.urls import reverse 

class Post(models.Model):
    body = models.CharField(max_length=27)
    author = models.ForeignKey('auth.User', related_name="chirp", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse("chirp:hom", args=(self.pk,))

    class Meta:
        ordering = ['-created']
    
    