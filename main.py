import asyncio

from ib_insync import *

from brokers.interactivebrokers.base import QQQ_USD_SMART
from brokers.interactivebrokers.broker import InteractiveBrokersBroker
from ib_bot_v7 import IB_Bot
from simstrat import SimpleStrategy

broker: InteractiveBrokersBroker = InteractiveBrokersBroker()
# broker.place_order(QQQ_USD_SMART(), Order(action='SELL', totalQuantity=500, orderType='MKT'))

strategy: SimpleStrategy = SimpleStrategy(broker)
bot: IB_Bot = IB_Bot(strategy.next)

try:
    asyncio.run(bot.run())
except (KeyboardInterrupt, SystemExit):
    bot.stop()
