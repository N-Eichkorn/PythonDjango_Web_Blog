from django.db import models

# Create your models here.
class Post(models.Model):
    headline = models.CharField(max_length=60)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.headline

class Comment(models.Model):
    author = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    date = models.DateTimeField('date published')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
