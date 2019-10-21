from django.urls import path
from .views import indexView, searchView

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('search/', searchView.as_view(), name='search'),
]
