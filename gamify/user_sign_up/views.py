from django.shortcuts import render

def sign_view(request):
    return render(request, "{% url 'sign' %}.html")