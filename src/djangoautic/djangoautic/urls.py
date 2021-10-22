"""djangoautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# import url (follow Ninja)
from django.conf.urls import url, include

''' import views.py we created '''
# from . >>>  from the curent directory you are in
from . import views


urlpatterns = [
    # url(page, callBcakfunction) >>>  when the user visits this page, it will fire this function

    # regular expression
    # r >> raw string
    # ^ >> the start of the string. it has to come directly after /  >>>  /admin  
    # $ >> the end of the string. /  >>> abmin has to be the end of the string
    path('admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),    #when the user visit .com, it fires homepage() in the views.py
    url(r'^articles/',include('articles.urls')),

]
