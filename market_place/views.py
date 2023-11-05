from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from market_place.forms import BookingDatesForm
from market_place.models import StorageBox
from market_place import filters



def main(request):
    form = BookingDatesForm(
        {
            "start_date": request.GET.get("start_date"),
            "end_date": request.GET.get("end_date"),
        }
    )
    if all(
        [request.GET.get("start_date"), request.GET.get("end_date"), form.is_valid()]
    ):
        qs = StorageBox.available_on_period(
            form.cleaned_data["start_date"],
            form.cleaned_data["end_date"],
        )
    elif not form.is_valid():
        messages.warning(request, _("The end date must be after the start date"))
        qs = StorageBox.objects.none()
    else:
        qs = StorageBox.objects.all()
    f = filters.StorageBoxFilter(request.GET, queryset=qs)
    
    # sort qs if filter is applied
    if f.form.changed_data:
        storage_boxes = f.qs.order_by(*f.form.changed_data)
    else:
        storage_boxes = f.qs

    context = {
        "page_title": _("Storage Voxes"),
        "filter": f,
        "storage_boxes": storage_boxes,
        "date_form": form,
        "start_date": request.GET.get("start_date"),
        "end_date": request.GET.get("end_date"),
    }
    return render(request, "marketplace/main.html", context)
