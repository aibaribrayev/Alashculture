from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    readmore = models.URLField(max_length=1000, default='')
    def __str__(self):
        return self.title
    #def summary(self):
    #    return self.body[:100]
