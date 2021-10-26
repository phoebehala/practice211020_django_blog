''' 
    models/fields. ---- field types
    CharField
    https://docs.djangoproject.com/en/1.11/ref/models/fields/ '''

from django.db import models
from django.db.models.fields import DateField, SlugField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    Slug = models.SlugField()   # s/b url friendly string
    body = models.TextField()
    date = models.DateTimeField( auto_now_add=True)
    # add in thumbnail late
    # add in author later

    # instance of Article
    def __str__(self):
        return self.title

    ''' model method '''
    def snippet(self):
                       # [:50] means [0:50] means from 0 to fiftieth character
        return self.body[:50]+"..."