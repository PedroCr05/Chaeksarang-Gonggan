from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TAGS = (
    ('A', 'Adventure'),
    ('C', 'Comedy'),
    ('D', 'Drama'),
    ('DC', 'Dystopian'),
    ('F', 'Fantasy'),
    ('H', 'Horror'),
    ('HIS', 'Historical'),
    ('MA', 'Martial Arts'),
    ('MM', 'Mecha'),
    ('MY', 'Mystery'),
    ('P', 'Psychological'),
    ('PAR', 'Paranormal'),
    ('R', 'Romance'),
    ('SF', 'Science Fiction'),
    ('SH', 'Superhero'),
    ('SL', 'Slice of Life'),
    ('SP', 'Sports'),
    ('TH', 'Thriller'),
    ('TR', 'Tragedy'),
    ('W', 'Western'),
)


class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    story = models.TextField()
    photo = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'story_id': self.id})

class Tag(models.Model):
    name = models.CharField(
        max_length=25,
        choices=TAGS,
        default=[0][0]
    )

    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tag_display()} on {self.name}"