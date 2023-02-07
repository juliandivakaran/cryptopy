import mplfinance as mpl
from api5 import df

#NORMAL CANDLE
mpl.plot(df, type='candle')

#DROW
mpl.plot(df, type='candle', volume=True, mav=7)