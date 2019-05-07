from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardForm
from django.http import HttpResponseRedirect

def show(request):
    boards = Board.objects
    # 블로그 모든 글들을 대상으로
    board_list = Board.objects.all().order_by('-id')
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,6)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'show.html', {'boards':boards, 'posts':posts})

def detail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board':board_detail})

# def post(request): # post.html을 띄워주는 함수
#     return render(request, 'post.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    if request.method == 'POST':
        board = Board()
        board.title = request.GET['title']
        board.updated_at = timezone.datetime.now()
        board.pwd = request.GET['pwd']
        board.save() #객채.delete()도 있다.
        return redirect('/board/'+str(board.id)) #redirect안에 url을 써줘야함.
        # board id는 int형. url은 string. 따라서 문자열로 형변환해줌

def boardpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST    
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # 저장하지 않고 모델객체를 반환
            post.updated_at = timezone.now()
            post.save()
            return redirect('show')
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BoardForm()
        return render(request, 'post.html', {'form':form})

def delete(request, board_id):
        board = Board.objects.get(pk=board_id)
        if board.pwd==request.GET['passwd']:
                board.delete()
                return redirect('show')
        else:
                return redirect('show')
