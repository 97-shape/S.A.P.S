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

def ShowChart(request, device_id):
    # print(device_id)
    queryset = {}
    if Device.objects.filter(id=request.user.id, device_id=device_id):
        queryset = Measurement.objects.filter(
            device_id = device_id
        ).values("measure_date", "measure", "predictive_measure", "measurement_accuracy")
    return render(request, 'chart.html', {'queryset':queryset, 'device_id':device_id});

"""
def ShowChart(request):
    devices = Device.objects.filter(
        id=request.user.id
    ).values("device_id");
    # print(devices[0])
    return render(request, 'chart.html', {'queryset':getData(devices[0])}, devices);

# 차트 데이터 받아오기
def getData(device):
    queryset = Measurement.objects.filter(
        device_id = device.get('device_id')
    ).values("measure_date", "measure")
    # print(queryset)
    return queryset
"""