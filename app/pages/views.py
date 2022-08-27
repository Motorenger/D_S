from django.shortcuts import render

from products.models import Product

def home_view(request):

    prod = Product.objects.get(id=2)
    prod_cat = prod.cat
    context = {
        "products": Product.objects.all(),
        "prod_cat": prod.size_foot.all(),
        
    }
    
    return render(request, 'pages/home.html', context=context)
