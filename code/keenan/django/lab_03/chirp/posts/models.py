from django.db import models
# import datetime? what models features require datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    post_body = models.CharField(max_length=128)
    author = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        # look up how to refer to the post with the author also
        return self.title
