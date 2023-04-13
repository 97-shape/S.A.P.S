from django.shortcuts import render

from database.models import Device, Measurement

# Create your views here.


def ShowData(request):
    devices = Device.objects.filter(
        id = request.user.id
    );
    return render(request, "list.html",{'device':devices});

def dashboard_display(request):
    return render(request, "dashboard_base.html");

def ShowChart(request):
    devices = Device.objects.filter(
        id=request.user.id
    ).values("device_id");
    queryset = {}
    for device in devices:
        queryset[device.get('device_id')] = Measurement.objects.filter(
            device_id = device.get('device_id')
        ).values("measure_date", "measure")
    return render(request, 'chart.html', {'queryset':queryset});