from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Portfolios
# Create your views here.

def index(request):
    portfolio = Portfolios.objects.all().order_by('created_at')
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/index.html', context)

def detail(request, port_id):
    portfolio = Portfolios.objects.get(id=port_id)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio/detail.html', context)

def new(request):
    return render(request, 'portfolio/new.html')

def create(request):
    author = request.POST['author']
    body = request.POST['body']
    port = Portfolios(author=author, body=body, created_at=timezone.now()) 
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

def edit(request, port_id):
    port = Portfolios.objects.get(id=port_id)
    context = {'port': port} 
    return render(request, 'portfolio/edit.html', context)

def update(request, port_id):
    port = Portfolios.objects.get(id=port_id)
    port.author = request.POST['author']
    port.body = request.POST['body']
    port.save()
    return redirect('portfolio:detail', port_id=port.id)

def delete(reqeust, port_id):
    port = Portfolios.objects.get(id=port_id)
    port.delete()
    return redirect('portfolio:index')