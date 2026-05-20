from django.urls import path
from .views import world_view, tools_home

app_name = "tools"

urlpatterns = [
    path("", tools_home, name="tools_home"),
    path("world/<int:world_id>/", world_view, name="world_view"),
]
