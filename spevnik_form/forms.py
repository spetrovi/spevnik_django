from django import forms
from .models import Metadata


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class SongForm(forms.ModelForm):
    #    your_name = forms.CharField(label="Your name", max_length=100)
    class Meta:
        model = Metadata
        fields = ("title", "gathered_date", "rhytm", "location")
