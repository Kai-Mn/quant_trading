from django import forms
from .models import Companies, Stocks


class StockForm(forms.Form):
    # stock_name = forms.CharField(label="Stock name", max_length=4)
    # class Meta:
    #     model = Stocks
        # fields = ['stock_name']

    stock_name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["stock_name"].queryset = Companies.objects.all()


    # stock_name = forms.ModelChoiceField(
    #     queryset=Companies.objects.all(),
    #     to_field_name='name',
    #     required=True,  
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )   