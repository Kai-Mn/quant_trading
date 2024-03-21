import django_tables2 as tables
from .models import Stocks, Results, Companies

class StocksTable(tables.Table):
    class Meta:
        model = Stocks
        
class CompaniesTable(tables.Table):
    name = tables.Column(linkify=True)
    your_field = tables.CheckBoxColumn(accessor="id")
    class Meta:
        model = Companies

class ResultsTable(tables.Table):
    simulation = tables.Column(linkify=True)
    
    class Meta:
        model = Results