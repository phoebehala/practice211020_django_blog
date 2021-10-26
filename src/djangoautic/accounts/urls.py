from django.conf.urls import url
from django.urls import path

''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views

app_name = "accountsApp"

urlpatterns = [
   
    path('signup/', views.signup_view, name="signup"),
  
]


