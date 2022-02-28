from operator import mod
from django.db import models

# Create your models here.

class PaperFile(models.Model):
    name=models.CharField(max_length=100)
    fingerprint=models.CharField(max_length=64) #sha256
    file=models.FileField(upload_to="uploadedPapers")
    
    def __str__(self):
        return self.name



