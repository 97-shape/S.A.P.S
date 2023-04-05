from django.shortcuts import render

# Create your views here.


def home_display(request):
    return render(request, 'base.html')