from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from ..models import Stocks
import pandas as pd


# Create a Stratey
#TODO put this in seperate file so we can exchange them easily
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])


def exec():
    cerebro = bt.Cerebro()
    # Add a strategy
    # cerebro.addstrategy(TestStrategy)

    # Load data from database
    df = pd.DataFrame(o.__dict__ for o in Stocks.objects.all())

    # Create datafeed
    data = df.to_csv()
    
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)


    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

