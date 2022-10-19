import asyncio
from typing import Callable

import pandas as pd
from ib_insync import *

# Symbols to get
contracts = [Crypto('BTC', 'PAXOS', 'USD')]
# contracts = [Forex('USDJPY', 'IDEALPRO')] 

# init dataframe
df = pd.DataFrame(columns=['date', 'last'])
df.set_index('date', inplace=True)


class IB_Bot:
    def __init__(self, callback: Callable) -> None:
        self.callback: Callable = callback

    async def run(self):
        self.ib = IB()

        with await self.ib.connectAsync(port=7497):
            for contract in contracts:
                self.ib.reqMktData(contract)

            async for tickers in self.ib.pendingTickersEvent:
                tickers: list[Ticker]
                for ticker in tickers:
                    # print(ticker.time, ticker.close)
                    df.loc[ticker.time] = ticker.last
                    resampled: pd.DataFrame = df['last'].resample('1s').ohlc()
                    self.callback(resampled.index[-1], resampled['close'][-1])

    def stop(self):
        self.ib.disconnect()


# Run Bot
if __name__ == "__main__":
    bot = IB_Bot()
    try:
        asyncio.run(bot.run())
    except (KeyboardInterrupt, SystemExit):
        bot.stop()
