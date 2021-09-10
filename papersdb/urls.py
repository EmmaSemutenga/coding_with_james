from django.urls import path
from papersdb.views import add_author, author_list, home_page, add_paper,checkmate

urlpatterns = [
    path('', home_page, name='home'),
    path('my_paper/', add_paper),
    path('add_author/', add_author, name = 'add_author'),
    path('authors/', author_list, name='authors'),
    path('checkmate/<int:id>/', checkmate),
]
