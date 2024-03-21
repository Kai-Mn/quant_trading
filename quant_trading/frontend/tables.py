import django_tables2 as tables
from .models import Stocks, Results, Companies

class StocksTable(tables.Table):
    class Meta:
        model = Stocks
        
class CompaniesTable(tables.Table):
    name = tables.Column(linkify=True)
    
    class Meta:
        model = Companies

class ResultsTable(tables.Table):
    simulation = tables.Column(linkify=True)
    
    class Meta:
        model = Results