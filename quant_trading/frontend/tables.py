import django_tables2 as tables
from .models import Stocks

class StocksTable(tables.Table):
    class Meta:
        model = Stocks  