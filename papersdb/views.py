from django.shortcuts import render
from my_project import hobbies
from .models import Paper

# Create your views here.
def home_page(request):
    papers = Paper.objects.all()
    return render(request, 'index.html', {"james_papers":papers})
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form of a dictionary.

# GET
# POST
# Client
# Server side rendering
# Client side rendering
# Application Programming Interface
# React
