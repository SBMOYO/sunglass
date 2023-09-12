from django.shortcuts import render
from .models import Sunglass

# Create your views here.
def index(request):
    sunglass = Sunglass.objects.all()
    return render(request, 'index.html',{'sunglass': sunglass})

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def glasses(request):
    return render(request, 'glasses.html')

def contact(request):
    return render(request, 'contact.html')
