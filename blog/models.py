from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #django default authentication framework


# Create your models here.
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,    #many-to-one relationship
                                on_delete=models.CASCADE,
                                related_name='blog_posts') 
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)

    class Meta:
        ordering = ['-publish'] #sort posts from newest to oldest, descending order
        indexes = [
            models.Index(fields=['-publish']), #improves performance for quesries filtering
        ]

    def __str__(self):
        return self.title