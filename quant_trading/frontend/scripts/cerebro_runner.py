from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import backtrader as bt
from ..models import Stocks
import numpy as np
import time
from .utils import convert_to_dataframe
from ..strategies.example_strategy import TestStrategy 



def exec():
    cerebro = bt.Cerebro()
    # Add a strategy
    cerebro.addstrategy(TestStrategy)    
    
    # Load data from database and convert it to a datafeed
    df = convert_to_dataframe(Stocks.objects.all(),fields=['open', 'high', 'low', 'close', 'volume', 'date'])
    df['date'] = df['date'].apply(lambda x: np.datetime64(time.strftime( '%Y-%m-%d', time.gmtime(x))))
    df.set_index('date', inplace=True)
    data = bt.feeds.PandasData(dataname=df)
    
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()
