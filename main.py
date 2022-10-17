import asyncio

from brokers.interactivebrokers.broker import InteractiveBrokersBroker
from ib_bot_v7 import IB_Bot
from simstrat import SimpleStrategy

broker: InteractiveBrokersBroker = InteractiveBrokersBroker()

strategy: SimpleStrategy = SimpleStrategy(broker)
bot: IB_Bot = IB_Bot(strategy.next)

try:
    asyncio.run(bot.run())
except (KeyboardInterrupt, SystemExit):
    bot.stop()
