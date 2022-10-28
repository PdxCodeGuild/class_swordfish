from django.db import models
from django.utils import timezone

class Posts(models.Model):
    post = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.post

    class Meta:
        ordering = ['-pub_date']
