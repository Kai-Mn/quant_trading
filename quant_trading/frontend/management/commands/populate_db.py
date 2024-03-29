from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import yfinance as yf
from django.conf import settings
from frontend.models import Stocks, Companies
import time
import django




class Command(BaseCommand):
    help = "Populates with financedata fetched from Yahoofinance based on the csv"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(options['path'])
            )
        short_list = pd.read_excel(options['path'][0])
        
        for index, row in short_list.iterrows():
            if row['Still Listed'] == True:
                symbol = row['SYMBOL']

                comp = {}
                if not Companies.objects.filter(name = symbol).exists():
                    comp = Companies.objects.create(name = symbol)
                    comp.save()
                else :
                    comp = Companies.objects.get(name = symbol)

                data = yf.download(symbol, period="1mo")

                #TODO we are looping over a pd.dataframe here which is an unperformant antipattern. This should be done in SQL
                models = []
                for index, row in data.iterrows():
                    models.append(
                        Stocks(
                        date=time.mktime(row.name.timetuple()),
                        open=row['Open'],
                        high=row['High'],
                        low=row['Low'],
                        close=row['Close'],
                        adj_close=row['Adj Close'],
                        volume=row['Volume'],
                        type_id=comp.id,
                        )
                    )

                for model in models:
                    if not Stocks.objects.filter(date = model.date , type = model.type.id):
                        model.save()
                        self.stdout.write(
                            self.style.SUCCESS("Successfully created entry for {0} with timestamp {1}".format(model.type.name, model.date))
                        )
                    else:
                        self.stderr.write(
                            self.style.ERROR("entry for {0} with timestamp {1} already exists".format(model.type.name, model.date))
                        )
