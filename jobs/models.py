from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    #body = models.TextField()
    #add links to facebook and email

    def __str__(self):
        return self.summary
