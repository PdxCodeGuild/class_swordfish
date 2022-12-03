from django.db import models

class Posts(models.Model):
    post_author = models.CharField(max_length=50)
    post_body = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_body