from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard_view(request):
    return render(request, "{% url 'dashboard' %}.html")

def quiz_view(request):
    return render(request, "{% url 'quiz' %}.html")

