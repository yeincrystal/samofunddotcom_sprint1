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