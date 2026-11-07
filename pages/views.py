from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def services_details(request):
    return render(request, 'services-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')