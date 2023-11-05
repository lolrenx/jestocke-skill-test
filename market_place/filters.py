from market_place.models import StorageBox

from django import forms
from django.db.models import Max
from django_filters import FilterSet, ChoiceFilter, NumberFilter


__all__ = ["StorageBoxFilter"]


SELECT_ATTRS ={"class": "select select-bordered select-sm mx-2"}


class StorageBoxFilter(FilterSet):
    city  = ChoiceFilter(widget=forms.Select(attrs=SELECT_ATTRS),
    )
    storage_type = ChoiceFilter(
        field_name="storage_type",
        widget=forms.Select(attrs=SELECT_ATTRS),
        label="Type",
    )
    surface__gte = NumberFilter(
        field_name='surface',
        lookup_expr='gte',
        label="Surface (m²) >=",
        widget=forms.NumberInput(
            attrs={
                "class": "input input-bordered input-sm w-24",
                "min": 1,
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters["city"].field.choices = sorted(
            [(c, c) for c in StorageBox.objects.values_list("city", flat=True).distinct()]
        )
        self.filters["storage_type"].field.choices = sorted(
            [(c, c) for c in StorageBox.objects.values_list("storage_type", flat=True).distinct()]
        )
        self.filters["surface__gte"].field.widget.attrs["max"] = StorageBox.objects.aggregate(Max("surface"))["surface__max"]

    class Meta:
        model = StorageBox
        fields = [
            "city",
            "storage_type",
            "surface__gte",
        ]
