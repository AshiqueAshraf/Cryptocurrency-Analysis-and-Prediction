import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
#class PriceCompareBTCStatusClass:
#   def plot_btc_status_price(self, plot_date):

cryptocurrency = ['BTC-USD']
data = yf.download(cryptocurrency)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close"]][data["Date"]=='2022-11-18']

print(data)
print(data["Open"])
open=data["Open"]
print(data["High"])
high=data["High"]
print(data["Low"])
low=data["Low"]
print(data["Close"])
close=data["Close"]

x = np.array(["Open", "High", "Low", "Close"])
y = np.array([open, high, low, close])
print(x)

print(y[0][0])
print(y[1][0])
print(y[2][0])
print(y[3][0])
con=str(y[0][0]) +","+str(y[1][0])+","+str(y[2][0])+","+str(y[3][0])
print("----------------")
print(data)
print(con)
print("-------------")
y1=[y[0][0],y[1][0],y[2][0],y[3][0]]

plt.bar(x,y1)
for bar in plots.patches:
    plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 5,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 5),
                   textcoords='offset points')

plt.show()