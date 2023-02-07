import pandas as pd
from bin import client


asset="SOLUSDT"
start="2023,1,1"
end="2023,2,6"
timeframe="1d"




df= pd.DataFrame(data=client.get_historical_klines(asset, timeframe,start,end))
df=df.iloc[:,:6]
df.columns=["Date","Open","High","Low","Close","Volume"]
df=df.set_index("Date")
df.index=pd.to_datetime(df.index,unit="ms")
df=df.astype("float")

print(df)


