from django import forms
from django.forms import DateInput


__all__ = [
    "BookingDatesForm",
]


class BookingDatesForm(forms.Form):
    start_date = forms.DateField(
        required=False, label="Start Date", widget=DateInput(attrs={"type": "date"})
    )
    end_date = forms.DateField(
        required=False, label="End Date", widget=DateInput(attrs={"type": "date"})
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date and start_date > end_date:
            self.add_error("start_date", "Start date must be before end date")
            self.add_error("end_date", "End date must be after start date")
        return cleaned_data
