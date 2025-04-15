from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from . forms import SignUpForm
# Create your views here.

def sign_up(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully")
            return redirect('/')
        else:
            print("Form Error", form.errors)
    else:
        form = SignUpForm()

    context = {
        "form": form
    }
    return render(request, 'users/signup.html', context)