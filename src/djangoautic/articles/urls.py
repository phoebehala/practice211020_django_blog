
# import url (follow Ninja)
from django.conf.urls import url


''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views

from django.urls.conf import path



urlpatterns = [
    url(r'^$',views.article_list),    #when the user visit .com, it fires homepage() in the views.py
    
    path('<slug:mySlug>/', views.article_detail),
    
  
]

