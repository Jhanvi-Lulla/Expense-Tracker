from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from tracker.models import expense
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            print(username)
            str= f'Welcome {username} !! Your Account has been created successfully!'
            form.save()
            messages.success(request, str)
        return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def user_posts(request):
    # Get the logged-in user (request.user will contain the logged-in user)
    user = request.user
    if user.is_authenticated:
        # Retrieve posts for the logged-in user
        posts = expense.objects.filter(created_by=user)
        print(posts,"--------------------------------")
        return render(request, 'tracker/index2.html', {'posts': posts})
    else:
        # If user is not authenticated, redirect to login page or show a message
        return render(request, 'users/login.html')
def custom_logout(request):
    logout(request)
    return render(request,'users/logout.html')
    




        

# Create your views here.
