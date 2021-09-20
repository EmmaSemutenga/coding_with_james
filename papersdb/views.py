from django.shortcuts import redirect, render
from my_project import hobbies # delete ?
from .models import Paper, Author
from .forms import PaperForm

# Create your views here.
def home_page(request):
    papers = Paper.objects.all()
    return render(request, 'index.html', {"james_papers":papers}) # The keys and the values are kind of the same, but the key is a string and the values are the values.
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form of a dictionary.

def add_paper(request):
    form = PaperForm()
    # print(request.method)
    return render(request, 'add_paper.html', {"james_form":form, "my_request": request.method, })

def add_author(request):
    if request.method == 'POST': # request is an object and method is one of the attributes it has. The data will be sent in the request object.
        author = request.POST['author_name'] # The POST object is a dictionary. This is not a link.
        Author.objects.create(name = author)
        return redirect('papersdb:author_list_page') # This name is available to views.py from urls.py. This is a link. return here can end the function if the if statement is True; if not the return on line 23 ends the function.
    #   print(request.POST["author_name"]) # print() is a Python function that will print to the terminal. This is often used for testing and debugging.                  
    return render(request, 'add_author.html') # This is like an else case.

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {"james_authors":authors})

def author_detail(request, id):
    print(request.method)
    print(id)
    author = Author.objects.get(id=id) # The id on the left is the column you want to check. The first = here is an assignment in Python; but the second = is an equals in SQL (i.e. what would be == in Py.)
    return render(request, 'author_detail.html', {"james_author_details":author})

def edit_author(request, id): # Here we receive a request and an id
    author = Author.objects.get(id=id)    
    if request.method == 'POST':
        author_name = request.POST['author_name'] # We are getting the submitted value from the form (activated when the Edit Author button is clicked).
        author.name = author_name # Here we update the name of the author object
        author.save()
        return redirect('papersdb:author_list_page')
    return render(request, 'edit_author.html', {"james_author_details":author}) # This will only run if the request is (e.g.) 'GET'.

def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('papersdb:author_list_page')