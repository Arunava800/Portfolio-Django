from django.shortcuts import render


# Create your views here.

def start_page(request):
    return render(request, 'mainpage/start_page.html')
