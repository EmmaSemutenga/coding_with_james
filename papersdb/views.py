from django.shortcuts import render

# Create your views here.
def home_page(request):
    print(request.method)
    return render(request, 'index.html', {"name":"James From Brighton"})

# GET
# POST
# Client
# Server side rendering
# Client side rendering
# Application Programming Interface
# React
