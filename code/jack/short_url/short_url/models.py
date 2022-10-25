from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    creation_ip = models.CharField(max_length=200)
    clicks = models.CharField(max_length=8)

    def __str__(self):
        return self.id

class Click(models.Model):
    # http_host = models.CharField(max_length=200) # request.HTTP_HOST
    client_ip = models.CharField(max_length=200)
    url = models.ForeignKey(Url, related_name="metadata", on_delete=models.CASCADE)

    def __str__(self):
        return self.id