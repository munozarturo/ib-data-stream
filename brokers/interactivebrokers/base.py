from ib_insync import *

from brokers.base import Dispatch, uids_range

InteractiveBrokersDispatch: Dispatch = Dispatch(
    "InteractiveBrokers", uids_range(1000, 1999), 1000)

# It makes more sense to use SMART contracts because they aren't
# routed to an exclusive exchange, meaning there is a larger
# trade pool to choose from.
# i.e. smart algorithms can be used to find the lowest price
#      in multiple exchanges.

# EXCHANGE
NVDA_USD_NYSE = lambda: Stock("NVDA", "NYSE", "USD")
SPY_USD_AMEX = lambda: Stock("SPY", "AMEX", "USD")
QQQ_USD_NYSE = lambda: Stock("QQQ", "NYSE", "USD")
DJI_USD_CME = lambda: Index("INDU", "CME", "USD")

# SMART
NVDA_USD_SMART = lambda: Stock("NVDA", "SMART", "USD")
SPY_USD_SMART = lambda: Stock("SPY", "SMART", "USD")
QQQ_USD_SMART = lambda: Stock("QQQ", "SMART", "USD")
DJI_USD_SMART = lambda: Index("INDU", "SMART", "USD")
