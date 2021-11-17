from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200, default='')
    position = models.TextField(default='')
    body = models.TextField(default='')
    field_name = models.URLField(max_length=1000)

    def __str__(self):
        return self.summary
