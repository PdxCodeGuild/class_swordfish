from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('auth.User', related_name = 'posts', on_delete = models.CASCADE)
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    
