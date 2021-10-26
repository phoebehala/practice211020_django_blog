from django.contrib import admin

from .models import Article
                    #Ariticle >>> class name in the models.py

# Register your models here.

# tell django we want our articles model apear in the admin area
# tell django to register st. on the admin site
admin.site.register(Article)