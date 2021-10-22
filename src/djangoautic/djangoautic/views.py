# allow us to send response to the user
from django.http import HttpResponse

#import render modules
from django.shortcuts import render


# when the user visits about page, we want to fire this function
def homepage(request):
    #send response back 
    # return HttpResponse('homepage')

    # Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

