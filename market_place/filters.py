from market_place.models import StorageBox

from django import forms
from django.db.models import Max
from django.utils.translation import gettext_lazy as _

from django_filters import FilterSet, ChoiceFilter, RangeFilter


__all__ = ["StorageBoxFilter"]


SELECT_ATTRS ={"class": "select select-bordered select-sm mx-2"}
INPUT_ATTRS = {"class": "input input-bordered input-sm ml-2 w-24"}


class StorageBoxFilter(FilterSet):
    city  = ChoiceFilter(widget=forms.Select(attrs=SELECT_ATTRS),
    )
    storage_type = ChoiceFilter(
        field_name="storage_type",
        widget=forms.Select(attrs=SELECT_ATTRS),
        label=_("Type"),
    )
    surface = RangeFilter(field_name='surface', label=_("Surface between"))
    monthly_price = RangeFilter(field_name="monthly_price", label=_("Monthly price between"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["city"].field.choices = sorted(
            [(c, c) for c in StorageBox.objects.values_list("city", flat=True).distinct()]
        )
        self.filters["storage_type"].field.choices = sorted(
            [(c, c) for c in StorageBox.objects.values_list("storage_type", flat=True).distinct()]
        )
        self.filters["surface"].field.widget.attrs["class"] = INPUT_ATTRS["class"]
        self.filters["surface"].field.widget.attrs["type"] = "number"
        self.filters["surface"].field.widget.attrs["min"] = 0
        self.filters["surface"].field.widget.attrs["max"] = StorageBox.objects.aggregate(Max("surface"))["surface__max"]
        self.filters["monthly_price"].field.widget.attrs["class"] = INPUT_ATTRS["class"]
        self.filters["monthly_price"].field.widget.attrs["type"] = "number"
        self.filters["monthly_price"].field.widget.attrs["min"] = 0

    class Meta:
        model = StorageBox
        fields = [
            "city",
            "storage_type",
            "monthly_price",
            "surface",
        ]
