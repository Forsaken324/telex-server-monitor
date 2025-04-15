from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)


    def __str__(self) -> str:
        return self.title