from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup_view(request):

    #UserCreationForm() >>> create a new instance of this form
    form = UserCreationForm()

    #{key, value} >>> the dictionary we can send down
    return render(request, 'accounts/signup.html', {'myForm':form})