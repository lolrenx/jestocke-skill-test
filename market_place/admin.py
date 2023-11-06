
# Register your models here.
from django.contrib import admin

from booking.models import Booking
from market_place.models import StorageBox


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


class OwnerFilter(admin.AllValuesFieldListFilter):
    template = "admin/owner_filter.html"


class SurfaceFilter(admin.SimpleListFilter):
    title = "Surface"
    parameter_name = "surface"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples representing different age ranges.
            Args:
                request: The request object.
                model_admin: The model admin object.
            Returns:
                A list of tuples representing age ranges.
        """
        return [
            ("0-5", "0-5"),
            ("5-10", "5-10"),
            ("10-15", "10-15"),
            ("15-20", "15-20"),
            (">20", ">20"),
        ]

    def queryset(self, request, queryset):
        """
        Filters the queryset based on the selected age range.
            Args:
                request: The request object.
                queryset: The queryset to filter.
            Returns:
                The filtered queryset.
        """
        if self.value() == "0-5":
            return queryset.filter(surface__range=(0, 5))
        if self.value() == "5-10":
            return queryset.filter(surface__range=(5, 10))
        if self.value() == "10-15":
            return queryset.filter(surface__range=(10, 15))
        if self.value() == "15-20":
            return queryset.filter(surface__range=(15, 20))
        if self.value() == ">20":
            return queryset.filter(surface__gt=20)


@admin.register(StorageBox)
class StorageBoxAdmin(admin.ModelAdmin):
    inlines = [
        BookingInline,
    ]
    list_display = (
        "id",
        "owner",
        # "storage_type", # omitted due to absence of data
        "surface",
        "monthly_price",
        "city",
    )
    list_filter = (
        SurfaceFilter,
        # ("surface", SurfaceFilter),
        ("owner__email", OwnerFilter),
    )
    ordering = ("-id",)
