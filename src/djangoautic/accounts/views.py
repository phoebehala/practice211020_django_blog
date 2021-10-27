from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
 
def signup_view(request):
 
   if request.method == 'POST':
 
       # take data and somehow validate
       form = UserCreationForm(request.POST)
      
       if form.is_valid():  # true >>> valid
           form.save()  # save data to the database
           return redirect('articlesApp:list')   # return to article app and url named 'list' in the urls.py of articles app
  
   else:
 
       #UserCreationForm() >>> create a new instance of this form
       form = UserCreationForm()
 
   #{key, value} >>> the dictionary we can send down
   return render(request, 'accounts/signup.html', {'myForm':form})
