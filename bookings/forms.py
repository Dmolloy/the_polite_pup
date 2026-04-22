from django import forms
from django.utils import timezone
from datetime import datetime
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["session", "date", "time", "notes"]

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:
            selected_datetime = datetime.combine(date, time)
            current_datetime = timezone.localtime().replace(tzinfo=None)

            if selected_datetime < current_datetime:
                raise forms.ValidationError(
                    "Please select a future date and time."
                )

        return cleaned_data