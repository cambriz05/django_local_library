# user_login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # Redirect to home or another page after successful login
            else:
                # If authentication fails
                return render(request, 'user_login/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()  # If GET request, display the login form

    return render(request, "{% url 'login' %}.html", {'form': form})
