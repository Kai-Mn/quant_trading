from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import backtrader as bt
from ..models import Stocks
import numpy as np
import time
from .utils import convert_to_dataframe
from ..strategies.example_strategy import TestStrategy 
import matplotlib



def exec(Strategy):
    #TODO fix for wrong backend being used by plot https://stackoverflow.com/questions/37604289/tkinter-tclerror-no-display-name-and-no-display-environment-variable
    matplotlib.use('Agg')
    cerebro = bt.Cerebro()
    # Add a strategy
    cerebro.addstrategy(Strategy)    
    
    # Load data from database and convert it to a datafeed
    df = convert_to_dataframe(Stocks.objects.all(),fields=['open', 'high', 'low', 'close', 'volume', 'date'])
    df['date'] = df['date'].apply(lambda x: np.datetime64(time.strftime( '%Y-%m-%d', time.gmtime(x))))
    df.set_index('date', inplace=True)
    data = bt.feeds.PandasData(dataname=df)

    # Add plotinfo to data
    plotinfo = dict(plot=True,
                subplot=True,
                plotname='',
                plotskip=False,
                plotabove=False,
                plotlinelabels=False,
                plotlinevalues=True,
                plotvaluetags=True,
                plotymargin=0.0,
                plotyhlines=[],
                plotyticks=[],
                plothlines=[],
                plotforce=False,
                plotmaster=None,
                plotylimited=True,
           )
 
    
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    plot = cerebro.plot()
    for index, figure in enumerate(plot[0]):
        return figure
        # figure.savefig("quant_trading/frontend/plots/figure_{}.png".format(index))
