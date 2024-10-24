from django.db import models
from django.contrib.auth.models import User


LANGS = (
    ('py', 'Python'),
    ('js', 'Javascript'),
    ('cpp', 'C++'),
    ('php', 'PHP')
)

BOOLS = (
    (True, 'Public'),
    (False, 'Private')
)

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True, choices=BOOLS)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, related_name='author_comment')
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
