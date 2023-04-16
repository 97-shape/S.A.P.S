from django.shortcuts import render

from database.models import Device, Measurement

# Create your views here.


def GetData(user_id):
    devices = Device.objects.filter(
        id = user_id
    );
    return devices;

def Dashboard_display(request):
    return render(request, "dashboard_base.html", {'device':GetData(request.user.id)});

def BoardList(request):
    return render(request, "board/board_list.html", {'device':GetData(request.user.id)});

def BoardWrite(request):
    return render(request, "board/board_write.html", {'device':GetData(request.user.id)});

# 차트 밑 표 구성을 위한 데이터 전송

def DisplayData(request, device_id):
    # print(device_id)
    queryset = {}
    if Device.objects.filter(id=request.user.id, device_id=device_id):
        queryset = Measurement.objects.filter(
            device_id = device_id
        ).values("measure_date", "measure", "predictive_measure", "measurement_accuracy")
    return render(request, 'chart.html', {'queryset':queryset, 'device_id':device_id, 'device':GetData(request.user.id)});