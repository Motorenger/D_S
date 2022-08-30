from django.shortcuts import render

from products.models import Product

def home_view(request):
    
    return render(request, 'pages/home.html')
