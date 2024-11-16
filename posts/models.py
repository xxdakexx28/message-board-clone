from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title