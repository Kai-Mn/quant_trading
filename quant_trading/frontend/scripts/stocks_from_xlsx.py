import pandas as pd
import yfinance as yf
from django.conf import settings
from frontend.models import Stocks, Companies
from sqlalchemy import create_engine
import time

def check_if_listed(path):
    short_list = pd.read_excel(path)
    still_listed = []
    stoped_listed = []
    for index, row in short_list.iterrows():
        info = yf.Ticker(row['SYMBOL']).history(
                                        period='1mo',
                                        interval='1wk')

        if len(info) > 0:
            still_listed.append('True')
        else:
            still_listed.append('False')

    short_list['Still Listed'] = still_listed
    with pd.ExcelWriter('stocks_with_listings.xlsx') as writer:
        short_list.to_excel(writer)
        print('Written unlisted/listed data to stocks_with_listings.xlsx')
    return short_list

def fetch_and_write_stocks(path):
    short_list = pd.read_excel(path)

    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']
    host = settings.DATABASES['default']['HOST']
    port = settings.DATABASES['default']['PORT']

    database_url = 'mariadb://{user}:{password}@db:3306/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
    )

    engine = create_engine(database_url, echo=False)

    #TODO make this asynchronous with cellery or such
    for index, row in short_list.iterrows():
        if row['Still Listed'] == True:
            symbol = row['SYMBOL']

            comp = {}
            #TODO if no stock exists create one then 
            if not Companies.objects.filter(name = symbol).exists():
                comp = Companies.objects.create(name = symbol)
                comp.save()
            else :
                comp = Companies.objects.get(name = symbol)

            data = yf.download(symbol, period="10y")
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


            Stocks.objects.bulk_create(models,ignore_conflicts=True)

