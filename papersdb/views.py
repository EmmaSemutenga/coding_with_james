from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from my_project import hobbies
from .models import Paper, Author
from .forms import PaperForm

# Create your views here.
def home_page(request):
    papers = Paper.objects.all()
    return render(request, 'index.html', {"james_papers":papers})
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form of a dictionary.

def add_paper(request):
    # if request.method == 'POST':
    #     print(list(request.POST['authors']))
    #     for author_id in request.POST['authors']:
    #         print(author_id)
    #     # if request.POST['title']
    # authors = Author.objects.all()
    form = PaperForm()
    if request.method == 'POST':
        form = PaperForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data.get("authors"))
    return render(request, 'add_paper.html', {"james_form":form, "my_request": request.method, })
    # return render(request, 'add_paperv2.html', {'authors':authors})

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Author.objects.create(name=name)
        return redirect('authors')
    return render(request, 'add_author.html')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors':authors})

def checkmate(request, id):
    print(id)
    paper = Paper.objects.get(id=id)
    if paper.published:
        paper.published = False
        paper.save()
    else:
        paper.published = True
        paper.save()
    return JsonResponse({'success':'object changed'})