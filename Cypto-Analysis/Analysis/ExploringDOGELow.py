import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

class ExploringDOGELowClass:
    def check(self):
        print("checked...")
    def doge_low_price(self,start_date,end_date):
        cryptocurrencies = ['DOGE-USD']
        data = yf.download(cryptocurrencies, start=start_date, end=end_date)
        data["Date"] = data.index
        data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]

        #print(data.head())
        #print(data['Date'].head(5))
        sns.set_theme(style="darkgrid")

        data['Date'] = pd.to_datetime(data['Date'])
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        sns.lineplot(x = "Date", y = "Low", data = data)
        plt.title('DOGE Low Price', fontsize=20, color='green')
        plt.xlabel("Low Price Dates", fontsize=17, color='blue')
        plt.ylabel("Low Price($)", fontsize=17, color='blue')
        fig = plt.gcf()
        fig.canvas.set_window_title('DOGE-Low Price')
        plt.show()
