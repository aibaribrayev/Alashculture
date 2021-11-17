from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    #add links to read more
    def __str__(self):
        return self.title
    #def summary(self):
    #    return self.body[:100]
