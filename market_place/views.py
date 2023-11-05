from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from market_place.models import StorageBox


def main(request):
    context = {
        "page_title": _("Storage Voxes"),
        "storage_boxes": StorageBox.objects.all(),
    }
    return render(request, "marketplace/main.html", context)
