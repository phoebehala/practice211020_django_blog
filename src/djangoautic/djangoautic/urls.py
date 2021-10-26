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


''' allow us to say where the media url is and where the document root is and it'll allow django to serve up this media files'''
from django.conf.urls.static import static
''' so that we can use pretty much access everything we defined in the settings.py'''
from django.conf import settings


# tell Django that it can serve up our static file (css, images, javascript) >>>  in reality, we hook it up with a service like AWS to serve our static file
# staticfiles_urlpatterns >>> let us append to the url pattern so that django can handle and serving up the static file
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


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
    
    path('accounts/', include('accounts.urls')),
]



# staticfiles_urlpatterns() >>> check if we are in debug mode. if we are, we'll append this thing right here. so that it knows how to serve up our own static file
urlpatterns += staticfiles_urlpatterns()

# static(media url, where the file stored)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 