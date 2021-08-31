from django.shortcuts import render

# Create your views here.
def home_page(request):
    print(request.method) # We want to know what method is being used.
    return render(request, 'index.html', {"name":"James From Brighton"})
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form or a dictionary.

# GET
# POST
# Client
# Server side rendering
# Client side rendering
# Application Programming Interface
# React
