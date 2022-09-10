from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64)
    is_done = models.BooleanField()

    def __str__(self):
        return f'{self.name}'
        