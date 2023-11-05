from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path, reverse_lazy

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("marketplace:main")),
        name="index",
    ),
    path(
        "marketplace/",
        include(("market_place.urls", "marketplace"), namespace="marketplace"),
    ),
    path("admin/", admin.site.urls),
]
