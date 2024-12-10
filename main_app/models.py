from django.db import models

class Stories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    story = models.TextField
    tags = models.ManyToOneRel
    photo = models.CharField
    