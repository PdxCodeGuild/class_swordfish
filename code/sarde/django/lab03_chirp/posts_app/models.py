from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    post_created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'auth.User', related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.post_text

