import django_tables2 as tables
from .models import Stocks, Results

class StocksTable(tables.Table):
    class Meta:
        model = Stocks  

class ResultsTable(tables.Table):
    simulation = tables.Column(linkify=True)
    
    class Meta:
        model = Results