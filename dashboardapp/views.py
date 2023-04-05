from django.shortcuts import render
from database.models import Device

# Create your views here.

def ShowData(request):
    devices = Device.objects.all();
    return render(request, "list.html",{'device':devices});
