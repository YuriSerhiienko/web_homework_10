import os
from django.db import models
from uuid import uuid4
# Create your models here.

def update_filename(instance, filename):
    upload_to = "upload"
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)

class Picture(models.Model):
    description = models.CharField(max_length=350)
    path = models.ImageField(upload_to=update_filename)

    def __str__(self):
        return f"{self.path}"