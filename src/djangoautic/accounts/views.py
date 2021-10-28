from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
 
def signup_view(request):
 
   if request.method == 'POST':
 
       # request.POST  >>> kinda the data we receive
       # take data and somehow validate
       form = UserCreationForm(request.POST)
      
       if form.is_valid():  # true >>> valid

            # log the user in 
                # form.save()  >>> save data to the database and return us the user
           user = form.save()
           login(request, user)
            
           return redirect('articlesApp:list')   # return to article app and url named 'list' in the urls.py of articles app
  
   else:
 
       #UserCreationForm() >>> create a new instance of this form
       form = UserCreationForm()
 
   #{key, value} >>> the dictionary we can send down
   return render(request, 'accounts/signup.html', {'myForm':form})




def login_view(request):
    if  request.method == 'POST':

        # sending the data into the function AuthenticationForm() and that's going to validate for us
       form = AuthenticationForm(data = request.POST)

       if form.is_valid():

            ''' log the user in ''' 
            user = form.get_user()
            login(request, user)

            return redirect('articlesApp:list')
        
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'myForm':form})


def logout_view(request):
    if request.method == 'POST':

        # log the current user out
        logout(request)
        return redirect('articlesApp:list')