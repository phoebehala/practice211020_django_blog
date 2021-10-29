# all of our model form for this articles app sill go inside this file
 
from django import forms
 
# . >>> means current directory
# to access our models.py
from . import models
 
# class CreateArticle inherits from  forms.ModelForm
class CreateArticle(forms.ModelForm):
   class Meta:
       # here is where we define how we want to output our form (which fields do we want to be present, which models de we want to inherit from)
       model = models.Article

       # you can write fields = '__all__' to add all fields in the model Instead of fields = ['title', 'body', 'slug', 'thumb']
       fields = ['title', 'body', 'slug', 'thumb']
       