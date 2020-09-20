from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    author = models.CharField( max_length=30, default='Ivona')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)

    objects = models.Manager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post',
                       args=[str(self.id)])
