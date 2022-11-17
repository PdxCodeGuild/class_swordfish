from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.title
