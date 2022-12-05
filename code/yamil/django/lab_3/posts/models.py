from django.db import models

class Posts(models.Model):
    post_body = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.post_body

