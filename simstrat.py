from datetime import datetime
from typing import Any, Iterable

import numpy as np
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
        
        self.historic: list = []
        
    def next(self, time: datetime, close: float) -> None: # , time: datetime | None, tickers: Ticker | Iterable[Ticker] | None
        self.historic.append(close)

        if len(self.historic) > 100:
            if np.average(self.historic[-60:]) > close and not self.bought:
                self.broker.place_order(QQQ_USD_SMART, Order(action='BUY', totalQuantity=500, orderType='MKT'))
                self.bought = True
                
            elif np.average(self.historic[-60:]) < close and self.bought and not self.sold:
                self.broker.place_order(QQQ_USD_SMART, Order(action='SELL', totalQuantity=500, orderType='MKT'))
                self.sold = True