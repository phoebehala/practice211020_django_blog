from django.conf.urls import url
from django.urls import path

''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views

app_name = "accountsApp"

urlpatterns = [

    #url(r'^signup/$', views.signup_view, name="signup"),
    path('signup/', views.signup_view, name="signup"),

    #url(r'^login/$', views.login_view, name="login"),
    path('login/', views.login_view, name="login"),

    #url(r'^logout/$', views.logout_view, name="login"),
    path('logout/', views.logout_view, name="logout"),


  
]


