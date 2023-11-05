from django.urls import path
from market_place import views


app = "marketplace"
urlpatterns = [
    path("", views.main, name="main"),
]
