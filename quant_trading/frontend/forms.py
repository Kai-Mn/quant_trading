from django import forms
from .models import Companies, Stocks


class StockForm(forms.Form):
    stock_name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["stock_name"].queryset = Companies.objects.all()
