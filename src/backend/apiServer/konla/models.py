#from django.db import models

# Create your models here.
# Written by Minyi Lei

""" # legacy model
class PaperFile(models.Model):
    name=models.CharField(max_length=100)
    fingerprint=models.CharField(max_length=64) #sha256
    file=models.FileField(upload_to="uploadedPapers")
    
    def __str__(self):
        return self.name
"""


