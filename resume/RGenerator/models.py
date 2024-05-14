from django.db import models

# Create your models here.

class Documents(models.Model):
    cover = models.FileField(upload_to='pdf-files')
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title