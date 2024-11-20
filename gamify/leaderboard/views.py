from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def leaderboard_view(request):
    return render(request, "leaderboard.html")

