from django.shortcuts import render
from .models import Shop

# Create your views here.
def index(request):
    ctx={
        'shop_list': Shop.objects.all(),
    }
    return render(request, 'baemin/index.html',ctx)
