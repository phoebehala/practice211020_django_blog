from django import forms
from django.shortcuts import redirect, render

# from .models  >>> from current directory and get models.py file
# Article >>> class name created inside of models.py
from .models import Article

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# . >>> curent directory
# import our own created forms.py
from . import forms


# Create your views here.
def article_list(request):
    # .order_by()
    articles =Article.objects.all().order_by('date')

    # output all data (aticles) to the templates
    # render(para1,para2,{}) >>> the third parameter is going to be the data that we want to send to the template
    # {key, value} >>> make the dictionary for the third parameter  
    return render(request, 'articles/article_list.html',{'articles':articles})

def article_detail(request,mySlug):
    #return HttpResponse(mySlug)

    # look for the Article in the database and return it to us an store in here (article variable)
    article = Article.objects.get(slug=mySlug)
    return render(request, 'articles/article_detail.html',{'eachArticle':article} )


# this is protecting article_create(request)  >>> u need to log in for this to work
# if the user doen't log in, it redirect the user to login page
@login_required(login_url="/accounts/login/")

def article_create(request): 
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
                                    # request.POST  >>> kinda the data we receive
                                    # take data and somehow validate
                                                # when we upload files, they don't come along with POST object. they come along with separate object FILES
       
        if form.is_valid():

            # save article to db
            # form.save() >>> return us that instance of that (article in this case)
            # commit=False >>> hang on a minute. we'll save it in a moment but don't commit to that action just yet, just give me that instance amd I'll do something with it then I'll save it
            myInstance = form.save(commit=False)

            # attach the author I log in to that instance
            myInstance.author = request.user
            myInstance.save()
            return redirect('articlesApp:list')
    else:
        # show empty form of creating Article
       form = forms.CreateArticle()


    # send that form to 'articles/article_create.html'
    return render(request, 'articles/article_create.html',{'formOfCreatedArticle':form})