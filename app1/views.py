from django.shortcuts import render, get_object_or_404 as go404
from .models import *
# Create your views here.

def home(request):
     qr = go404(Website,pk=1)
     return render(request, 'home.html', locals())

def menu(request):
    familias = Familia.objects.all()
    productos = Producto.objects.all()
    familias_no_vacias=()
    y=list(familias_no_vacias)
    for i in familias:
        count=0
        for j in productos:
            if j.tipo.name==i.name:
                count=+1
        if count!=0:
            y.append(i.name)

    print('Familias ===> ', y)
    qr = go404(Website,pk=1)
    
    return render(request,'Menu.html',locals())

def detail(request,pk):
    qr = go404(Website,pk=1)
    producto = Producto.objects.get(pk=pk)
    return render(request,'Detail.html',locals())