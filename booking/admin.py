# Register your models here.
from django.contrib import admin

from booking.models import Booking


class DropdownFilter(admin.AllValuesFieldListFilter):
    template = "admin/dropdown_filter.html"
    title = "StorageBox id"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tenant",
        "storage_box",
        "start_date",
        "end_date",
    )
    list_filter = (("storage_box__id", DropdownFilter),)
