from django.urls import path
from .views import world_view

app_name = "tools"

urlpatterns = [
    path("world/<int:world_id>/", world_view, name="world_view"),
]
