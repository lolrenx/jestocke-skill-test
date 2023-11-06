
# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest

from booking.models import Booking
from market_place.models import StorageBox


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


class OwnerFilter(admin.AllValuesFieldListFilter):
    template = "admin/owner_filter.html"


class CityFilter(admin.AllValuesFieldListFilter):
    template = "admin/dropdown_filter.html"

class PriceFilter(admin.SimpleListFilter):
    title = "Price"
    parameter_name = "monthly_price"

    def lookups(self, request: HttpRequest, model_admin: ModelAdmin) -> list[tuple[str, str]]:
        """
        Returns a list of tuples representing different price ranges.
            Args:
                request: The request object.
                model_admin: The model admin object.
            Returns:
                A list of tuples representing price ranges.
        """
        return [
            ("0-20", "0-20"),
            ("20-40", "20-40"),
            ("40-60", "40-60"),
            ("60-80", "60-80"),
            ("80-100", "80-100"),
            (">100", ">100"),
        ]
    
    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        """
        Filters the queryset based on the selected price range.
            Args:
                request: The request object.
                queryset: The queryset to filter.
            Returns:
                The filtered queryset.
        """
        if self.value() == "0-20":
            return queryset.filter(monthly_price__range=(0, 20))
        if self.value() == "20-40":
            return queryset.filter(monthly_price__range=(20, 40))
        if self.value() == "40-60":
            return queryset.filter(monthly_price__range=(40, 60))
        if self.value() == "60-80":
            return queryset.filter(monthly_price__range=(60, 80))
        if self.value() == "80-100":
            return queryset.filter(monthly_price__range=(80, 100))
        if self.value() == ">100":
            return queryset.filter(monthly_price__gt=100)

class SurfaceFilter(admin.SimpleListFilter):
    title = "Surface"
    parameter_name = "surface"

    def lookups(self, request: HttpRequest, model_admin: ModelAdmin) -> list[tuple[str, str]]:
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

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
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
        PriceFilter,
        ("owner__email", OwnerFilter),
        ("city", CityFilter),
    )
    ordering = ("-id",)
