from django.db import models
from django.urls import reverse
from chirp_project.settings import AUTH_USER_MODEL


class Chirp(models.Model):
    tiny_body = models.CharField(max_length=127)
    author = models.ForeignKey(AUTH_USER_MODEL, related_name="chirps", on_delete=models.CASCADE)

    def __str__(self):
        return self.tiny_body + " : " + str(self.id)

    def get_absolute_url(self):
        return reverse("chirps:detail", args=(self.pk,))
    