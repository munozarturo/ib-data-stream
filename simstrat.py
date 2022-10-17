from datetime import datetime
from typing import Any, Iterable

from ib_insync import *

from _utils.validation import val_instance
from brokers.interactivebrokers import InteractiveBrokersBroker
from brokers.interactivebrokers.base import QQQ_USD_SMART


class SimpleStrategy:
    def __init__(self, broker: InteractiveBrokersBroker):
        val_instance(broker, InteractiveBrokersBroker)
        
        self.broker = broker
        self.c: int = 0
        
        self.bought = False
        self.sold = False
        
    def next(self, *args: Any) -> None: # , time: datetime | None, tickers: Ticker | Iterable[Ticker] | None
        for arg in args:
            print(arg)
        
        self.c += 1
        
        if self.c > 300 and not self.bought:
            self.broker.place_order(QQQ_USD_SMART, Order(action='BUY', totalQuantity=500, orderType='MKT'))
            self.bought = True
        elif self.c > 600 and not self.sold:
            self.broker.place_order(QQQ_USD_SMART, Order(action='SELL', totalQuantity=500, orderType='MKT'))
            self.sold = True