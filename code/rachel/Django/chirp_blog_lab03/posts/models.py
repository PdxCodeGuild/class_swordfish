from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.pk,))
    