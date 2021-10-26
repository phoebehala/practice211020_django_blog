from django.shortcuts import render

# from .models  >>> from current directory and get models.py file
from .models import Article

from django.http import HttpResponse



# Create your views here.
def article_list(request):
    # .order_by()
    articles =Article.objects.all().order_by('date')

    # output all data (aticles) to the templates
    # render(para1,para2,{}) >>> the third parameter is going to be the data that we want to send to the template
    # {key, value} >>> make the dictionary for the third parameter  
    return render(request, 'articles/article_list.html',{'articles':articles})

def article_detail(request,mySlug):
    return HttpResponse(mySlug)

