from django.db import models

# Create your models here.
class Chirps(models.Model):
    chirp = models.CharField(max_length=250)
    date_made = models.DateTimeField(auto_now_add=True)
    chirper = models.ForeignKey('auth.User', related_name="chirps", on_delete=models.CASCADE)

    def __str__(self):
        return self.chirp

    class Meta:
        ordering = ['-date_made']