from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def dashboard_view(request):
    return render(request, "{% url 'dashboard' %}.html")

def user_profile_view(request):
    return render(request, "{% url 'user_profile' %}.html")

