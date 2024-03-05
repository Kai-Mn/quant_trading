from django import forms


class StockForm(forms.Form):
    stock_name = forms.CharField(label="Stock name", max_length=4)
