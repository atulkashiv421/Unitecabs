from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "trip_type",
            "pickup",
            "drop",
            "pickup_date",
            "pickup_time",
            "return_date",
            "return_time",
            "phone",
        ]

        widgets = {

            "trip_type": forms.HiddenInput(),

            "pickup": forms.TextInput(attrs={
                "placeholder": "Pickup Location"
            }),

            "drop": forms.TextInput(attrs={
                "placeholder": "Drop Location"
            }),

            "pickup_date": forms.DateInput(attrs={
                "type": "date"
            }),

            "pickup_time": forms.TimeInput(attrs={
                "type": "time"
            }),

            "return_date": forms.DateInput(attrs={
                "type": "date"
            }),

            "return_time": forms.TimeInput(attrs={
                "type": "time"
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "Contact Number"
            }),

        }