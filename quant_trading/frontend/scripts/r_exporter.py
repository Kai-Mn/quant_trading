from frontend.models import Stocks, Companies
import pandas as pd
import time
import numpy as np
from .utils import convert_to_dataframe


def stock_export_to_csv(symbol):
    # for company in Companies.obejcts():
    company = Companies.objects.get(name = symbol)
    stocks = convert_to_dataframe(Stocks.objects.filter(type = company.id),fields=['date','adj_close'])
    stocks['date'] = stocks['date'].apply(lambda x: np.datetime64(time.strftime( '%Y-%m-%d', time.gmtime(x))))
    stocks.to_csv('stock_x.csv', index=False)
    # with pd.ExcelWriter('stocks_with_listings.xlsx') as writer:
    #     stocks.to_csv(writer)
    #     print('Wr.xlsx')


# Date Stocks
# <date> <adj_close>