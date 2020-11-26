from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Portfolios
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    portfolio = Portfolios.objects.all().order_by('created_at')
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/index.html', context)

def detail(request, port_id):
    portfolio = Portfolios.objects.get(id=port_id)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/detail.html', context)

@login_required
def new(request):
    #로그인 되어있지 않으면 로그인 페이지로 보내기 
    #login if문 대신에 그냥 로그인을 조건화하는 decorative code 
    #if not request.user.is_authenticated:
     #   return redirect('accounts:login') <= decorator 안에 accounts 앱 안의 login으로 가게 하기 때문에 앱을 만들 때 이름을 accounts로 하는 것 

    return render(request, 'portfolio/new.html')
#Question: 왜 여기서 한 번 더 해줘야 해? =========================================================Q 
@login_required
def create(request):
   # if not request.user.is_authenticated:
    #    return redirect('accounts:login')

    user = request.user #모든 유저는 request.user 안에 있음 
    body = request.POST['body']

    image = None #에러방지-Nullable variable 
    if 'image' in request.FILES:
        image = request.FILES['image']

    port = Portfolios(user=user, body=body, image=image, created_at=timezone.now()) 
    port.save()
    return redirect('portfolio:detail', port_id=port.id)
#-------------------------------------SEARCH FUNCTION-----------------------------
#Question) index함수 안에 만들어야하나? 
def search(request):
    if request.method == "POST":
        author = request.POST["fund"] #Question) input tag의 name을 넣는게 맞는지 확인
        #검색결과에 일치하는 author이 있는지 확인 
        fund = Portfolios.objects.get(author = author)
        if not fund:
            body = request.POST["fund"]
            #검색결과와 일치하는 body가 있는지 확인
            fund = Portfolios.objects.get(body = body)
        context = {'fund':fund}

        #찾은 검색결과랑 전체 리스트 전부 보여주기         
        return render(request, "portfolio/index.html", context)
    #get방식일 때는 다시 index함수로 가도록 하기 
    else:
        return render('portfolio:index')
#----------------------------------------------------------------------------------

@login_required
def edit(request, port_id):
    try:
        port = Portfolios.objects.get(id=port_id, user=request.user)
    except Portfolios.DoesNotExist:
        return redirect('portfolio:index')       
    context = {'port': port} 
    return render(request, 'portfolio/edit.html', context)

@login_required
def update(request, port_id):
    try:
        port = Portfolios.objects.get(id=port_id, user=request.user)
    except Portfolios.DoesNotExist:
        return redirect('portfolio:index')
    #port.author = request.POST['author']
    port.body = request.POST['body']
    if 'image' in request.FILES:
        port.image = request.FILES['image']
    port.save()
    return redirect('portfolio:detail', port_id=port.id)

@login_required
def delete(reqeust, port_id):
    try:
        port = Portfolios.objects.get(id=port_id)
    #Question: 여기서 왜 except error아니고?? ====================================Q 
    #Get함수에 대한 예외: DoesNotExist 
    except Portfolios.DoesNotExist:
        return redirect('portfolio:detail')
    port.delete()
    return redirect('portfolio:index')


#==========복습/==========
@login_required
def like(request, port_id):

    if request.method == 'POST':
        try:
            port = Portfolios.objects.get(id=port_id)

            if request.user in port.liked_users.all():
                port.liked_users.remove(request.user)
            else:
                port.liked_users.add(request.user)

            return redirect('portfolio:detail', port_id=port.id)

        except Portfolios.DoesNotExist:
            pass

    return redirect('portfolio:index')