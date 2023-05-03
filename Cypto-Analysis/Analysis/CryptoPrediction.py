#Relative price changes of the cryptocurrencies

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

pd.set_option("display.max_columns",40)

# list of crptocurrencies as ticker arguments
#cryptocurrencies = ['BNB-USD','BTC-USD', 'ETH-USD','DOGE-USD','ATOM-USD']
cryptocurrencies = ['BTC-USD']
data = yf.download(cryptocurrencies)
#print(data)
data["Date"] = data.index
print(data.columns)

#print(data[['Date','Close']].head(4))
print(data[['Date','Close']].tail())
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]

sns.lineplot(x = "Date", y = "Close", data = data)

plt.title('BTC-USD')
plt.xlabel("Date")
plt.ylabel("BTC Close")
plt.show()



























