from django.db import models

class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    story = models.TextField()
    photo = models.TextField()

    def __str__(self):
        return self.name
