from django.db import models
# import datetime? what models features require datetime
from users.models import CustomUser


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    post_body = models.CharField(max_length=128)
    # auth.user links the post to the user model in the auth app
    #
    # related_name allows u to access all of the posts by an auther by user.posts
    # the default is users.modelnam_set but we assign it a new location
    # on_delete is what happens if an author user is deleted, if an author is delete all posts are deleted
    author = models.ForeignKey(CustomUser, related_name="posts", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # look up how to refer to the post with the author also
        return self.title
