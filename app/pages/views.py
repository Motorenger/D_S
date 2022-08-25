from django.shortcuts import render

from products.models import Product

def home_view(request):
    context = {
        "products": Product.objects.all(),
    }
    
    return render(request, 'pages/home.html', context=context)
