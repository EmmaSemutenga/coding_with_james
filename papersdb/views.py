from django.shortcuts import render
from my_project import hobbies
from .models import Paper
from .forms import PaperForm

# Create your views here.
def home_page(request):
    papers = Paper.objects.all()
    return render(request, 'index.html', {"james_papers":papers})
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form of a dictionary.

def add_paper(request):
    form = PaperForm()
    # print(request.method)
    return render(request, 'add_paper.html', {"james_form":form, "my_request": request.method, })

