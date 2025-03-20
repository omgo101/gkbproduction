from django.urls import path
from .views import login_view, home_view,search_view

urlpatterns = [
    path("", login_view, name="login"),
    path("home/", home_view, name="home"),
    path('search/',search_view, name='search'),
]
