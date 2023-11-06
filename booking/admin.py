from django.contrib import admin

from booking.models import Booking


class BoxFilter(admin.AllValuesFieldListFilter):
    template = "admin/storage_box_filter.html"


class TenantFilter(admin.AllValuesFieldListFilter):
    template = "admin/tenant_filter.html"


class OwnerFilter(admin.AllValuesFieldListFilter):
    template = "admin/owner_filter.html"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tenant",
        "storage_box",
        "start_date",
        "end_date",
    )
    list_filter = (
        ("storage_box__id", BoxFilter),
        ("tenant__email", TenantFilter),
        ("storage_box__owner__email", OwnerFilter),
    )
