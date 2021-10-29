
# import url (follow Ninja)
from django.conf.urls import url


''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views

from django.urls.conf import path


app_name = "articlesApp"

urlpatterns = [
    url(r'^$',views.article_list, name="list"),    #when the user visit .com, it fires homepage() in the views.py
    
    path('create/', views.article_create, name="create"),

   # approach 1- from ninja (does not work)
   # (?P< the-name-we-want-to-capture_eg. slug > what-can-the-slug-be-in-the-url)   a named capturing group
   # set another url for our article detail page that will be a page shows details of one particular article
   # regex (Ninja's approach)
       # \w >>> any kinds of letter
       # + >>> can be any length
#re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail),
 
    # approach 2- in Django 3
    # where the first slug "<slug" is the type of the passed parameter which is a slug in our case, and the second slug ":slug>" is the name of the parameter which could be any name; "abc", "the_slug", etc. If you still insist on using regex then there is one thing to change; the method name instead of "url" use "re_path": re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),'''
    path('<slug:mySlug>/', views.article_detail, name="detail"),

    
  
]

