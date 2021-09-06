from django.urls import path
from papersdb.views import home_page, add_paper

urlpatterns = [
    path('', home_page),
    path('my_paper/', add_paper),
]
