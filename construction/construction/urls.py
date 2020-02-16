
from django.contrib import admin
from django.urls import path

from django.shortcuts import HttpResponse,render

# def homepage(request):
#     return HttpResponse('Hello Django')
def homepage(request):
    a={
        "x":2000,
        "p":"Price",
    }
    return render(request,'index.html',a)

def service(request):
    return render(request,'service.html')

def conatct(request):
    return HttpResponse('This is my contact page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('contact/', conatct),
    path('service/', service),
]
