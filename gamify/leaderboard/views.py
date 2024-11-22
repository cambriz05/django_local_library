from django.shortcuts import render, HttpResponse

# Create your views here.
def user_profile_view(request):
    return render(request, "{% url 'user_profile' %}.html")

def leaderboard_view(request):
    return render(request, "leaderboard.html")

