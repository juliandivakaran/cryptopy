import pandas as pd
from bin import client
df = pd.DataFrame(client.get_all_tickers())
df=df.set_index("symbol")
df["price"]=df["price"].astype("float")
df.index=df.index.astype("string")
print(df)

print(df.loc["SOLUSDT"])