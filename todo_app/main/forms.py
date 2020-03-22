from django import forms
from .models import List

class List_Forms(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item_main", "completed"]