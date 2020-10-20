from django.db import models

class DropBox(models.Model):
    fileName = models.CharField(max_length=50)
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.fileName