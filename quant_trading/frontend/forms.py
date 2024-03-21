from django import forms
import os
from .models import Companies, Stocks, Simulations


class StockForm(forms.Form):
    stock_name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["stock_name"].queryset = Companies.objects.all()


class SimulationForm(forms.ModelForm):
    class Meta:
        model = Simulations
        fields = '__all__'

    strategy = forms.ChoiceField()
    company = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        #TODO this doesnt guarantee it only lists files
        files = [[file, file] for file in os.listdir('quant_trading/frontend/strategies')]
        self.fields["strategy"].choices = files
        names = [[company.id, company.name] for company in set(company for company in Companies.objects.all())]
        self.fields["company"].choices = names
