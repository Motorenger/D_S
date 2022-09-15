from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product

def home_view(request):
    print(request.COOKIES)
    request.COOKIES["user_attends"] = "hello world"
    responce = render(request, 'pages/home.html')
    responce.set_cookie('user_attends', "hello world")
    print(responce.cookies)
    return responce