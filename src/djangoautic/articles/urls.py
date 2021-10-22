
# import url (follow Ninja)
from django.conf.urls import url

''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views


urlpatterns = [
    url(r'^$',views.article_list),    #when the user visit .com, it fires homepage() in the views.py
    
]