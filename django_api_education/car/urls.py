from . import views
from django.urls import path, re_path

urlpatterns = [
    path("list", views.get_cars_list, name="cars"),
    path("", views.action_with_car),
    path("<str:id>", views.action_with_car),
]
