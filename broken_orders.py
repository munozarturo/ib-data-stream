from ib_insync import *

from brokers.interactivebrokers.base import QQQ_USD_SMART
from brokers.interactivebrokers.broker import InteractiveBrokersBroker

broker: InteractiveBrokersBroker = InteractiveBrokersBroker()

broker.place_order(QQQ_USD_SMART(), Order(action='BUY', totalQuantity=500, orderType='MKT'))

broker.place_order(QQQ_USD_SMART(), Order(action='SELL', totalQuantity=500, orderType='MKT'))

"""
* Try other order types.
"""