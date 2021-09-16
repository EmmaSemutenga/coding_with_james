from django.urls import path
# from papersdb.views import home_page, add_paper, add_author, author_list
from . import views # . here is the current directory, which is papersdb, and here we import the whole views module.

app_name = 'papersdb' # We add this here because if you end up with e.g. 10 apps in a project, naming paths can get messy and you can unwillingly double
# up. This is called URL NAME SPACING.

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('my_paper/', views.add_paper), # We need to add views. here if you use line 3 above instead of line 2.
    path('author/', views.add_author), # The first argument here is the address in the url/address bar which links to this. If this is matched the view is called.
    path('list_of_authors/', views.author_list, name='author_list_page'),
    path('author_details/<int:id>/', views.author_detail, name='author_detail'),
]
