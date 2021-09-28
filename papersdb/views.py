import papersdb # In grey means not used.
from django.shortcuts import redirect, render
from .models import Paper, Author
from .forms import AuthorForm, PaperForm

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html') # No objects are needed here.

def paper_list(request):
    papers = Paper.objects.all()
    return render(request, 'index.html', {"james_papers":papers}) # The keys and the values are kind of the same, but the key is a string and the values are the values.
    # render() takes 3 arguments: the original request, the template name, and any other data you want to send to the template in the form of a dictionary.

def add_paper(request):
    form = PaperForm()
    # print(request.method)
    return render(request, 'add_paper.html', {"james_form":form, "my_request": request.method, })

def add_author(request):
    form = AuthorForm() # an instance of a (form) class creating an object and assigned to the variable 'form'.
    if request.method == 'POST': # request is an object and method is one of the attributes it has. The data will be sent in the request object.
        form = AuthorForm(request.POST)
        if form.is_valid(): # We are checking the validity of form submitted on line 23
            author = form.cleaned_data.get('author_name') # author_name comes from line 15 of forms.py
            Author.objects.create(name = author)
            return redirect('papersdb:author_list_page') # This name is available to views.py from urls.py. This is a link. return here can end the function if the if statement is True; if not the return on line 23 ends the function.
    # print(request.POST["author_name"]) # print() is a Python function that will print to the terminal. This is often used for testing and debugging.                  
    return render(request, 'add_author.html', {"pineapple":form}) # This is like an else case.

def edit_author(request, id): # Here we receive a request and an id
    author = Author.objects.get(id=id) # Author is a (model) class; objects is an attribute of Author; get is a method.
    form_get = AuthorForm(instance=author)
    if request.method == 'POST':
        form_post = AuthorForm(request.POST, instance=author)
        if form_post.is_valid():
            # author_name = form_post.cleaned_data.get('author_name') Without Meta, we have to specify the link between the form and the database, so we need this line and the 2 lines below.
            # author.name = author_name
            # author.save() # To save the whole object
            form_post.save()
            #author = form.cleaned_data.get('author_name') # We are getting the submitted value from the form (activated when the Edit Author button is clicked).
            return redirect('papersdb:author_list_page') # Go back to the author list page after saving.
    return render(request, 'edit_author.html', {"strawberry":form_get}) # This will only run if the request is (e.g.) 'GET'.
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {"james_authors":authors})

def author_detail(request, id):
    print(request.method)
    print(id)
    author = Author.objects.get(id=id) # The id on the left is the column you want to check. The first = here is an assignment in Python; but the second = is an equals in SQL (i.e. what would be == in Py.)
    return render(request, 'author_detail.html', {"james_author_details":author})

def delete_author(request, id):
    author = Author.objects.get(id=id)
    author.delete()
    return redirect('papersdb:author_list_page')

def confirm_delete(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'confirm_delete.html', {"james_author_details":author})

