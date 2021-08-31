from django.urls import path
from papersdb.views import home_page

urlpatterns = [
    path('', home_page),
]
