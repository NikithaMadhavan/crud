from django.db import models

# Create your models here.
class Task(models.Model):
    slno=models.IntegerField()
    name=models.CharField(max_length=500)
    desc=models.TextField(max_length=1000)

    def __str__(self):
        return self.name