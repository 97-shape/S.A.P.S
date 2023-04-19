from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from dashboardapp.form import BoardWriteForm
from database.models import Device, Measurement, Board, UserData


# Create your views here.

# 장치 정보 받아오기
def GetData(user_id):
    devices = Device.objects.filter(
        id = user_id
    );
    return devices;
# 현제 이용자가 작성자가 맞는가?
def is_writer(user_id, board_writer):
    return True if user_id == str(board_writer) else False
# (임시)
def Dashboard_display(request):
    return render(request, "dashboard_base.html", {'device':GetData(request.user.id)});

# 게시판
def NoticeList(request):
    boards, paginator = BoardList('notice', request.GET.get('page'))
    return render(request, "board/board_list.html", {'boards': boards, 'paginator': paginator, 'board_type': 'notice', 'device': GetData(request.user.id)});

def FAQList(request):
    boards, paginator = BoardList('FAQ', request.GET.get('page'))
    return render(request, "board/board_list.html", {'boards': boards, 'paginator': paginator, 'board_type': 'FAQ', 'device': GetData(request.user.id)});

def BoardList(board_type, page):
    boards = Board.objects.filter(
        board_type = board_type
    ).order_by('-board_id');
    paginator = Paginator(boards, 1)

    try:
        page_board = paginator.page(page)
    except PageNotAnInteger:
        page_board = paginator.page(1)
    return page_board, paginator

def BoardWrite(request, board_type):
    print(board_type)
    context = {}
    if request.user.id:
        if request.method == 'GET':
            write_form = BoardWriteForm()
            context['forms'] = write_form
            return render(request, 'board/board_write.html', context, {'device':GetData(request.user.id)})

        elif request.method == 'POST':
            write_form = BoardWriteForm(request.POST)
            if write_form.is_valid():
                from datetime import datetime
                board = Board(
                    title = write_form.title,
                    content = write_form.content,
                    writer = UserData.objects.get(id=request.user.id),
                    write_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    board_type = board_type,
                )
                board.save()
                return redirect('/dashboard/' + board_type)
        else:
            return HttpResponse('Invalid Request')
    return HttpResponse('Invalid Request')

def BoardContent(request, board_type, board_id):
    previous_url = request.META.get('HTTP_REFERER', '/')  # 이전 목록으로
    board = Board.objects.get(
        board_id = board_id
    )

    return render(request, 'board/board_content.html',{'board':board, 'device': GetData(request.user.id),
                                                       'previous_url': previous_url, 'is_writer' : is_writer(request.user.id, board.writer)})


def BoardDelete(request, board_type, board_id):
    # 게시글 객체 가져오기
    board = get_object_or_404(Board, board_type=board_type, board_id=board_id)
    # 삭제
    board.delete()
    if board_type == 'notice':
        return redirect('dashboardapp:notice')
    elif board_type == 'FAQ':
        return redirect('dashboardapp:FAQ')
    else:
        return HttpResponse('Invalid Request')

def BoardEdit(request, board_id):
    board = get_object_or_404(Board, board_id=board_id)
    if request.method == 'POST':
        form = BoardWriteForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('dashboardapp:content', board_id=board_id, board_type=board.board_type)
    else:
        form = BoardWriteForm(instance=board)
    return render(request, 'board/board_edit.html', {'form': form, 'board_id': board_id, 'writer': board.writer,
                                                     'is_writer': is_writer(request.user.id, board.writer)})

# 차트 밑 표 구성을 위한 데이터 전송
def DisplayData(request, device_id):
    # print(device_id)
    queryset = {}
    if Device.objects.filter(id=request.user.id, device_id=device_id):
        queryset = Measurement.objects.filter(
            device_id = device_id
        ).values("measure_date", "measure", "predictive_measure", "measurement_accuracy")
    return render(request, 'chart.html', {'queryset':queryset, 'device_id':device_id, 'device':GetData(request.user.id)});