from app.views import root_view, teams_view
from django.urls import path

urlpatterns = [
    path("", root_view, name="root"),
    path("<str:team>", teams_view, name="teams")
]
