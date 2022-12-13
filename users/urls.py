from django.urls import path
from .views import *

urlpatterns = [path("users/", UsersView.as_view())]
