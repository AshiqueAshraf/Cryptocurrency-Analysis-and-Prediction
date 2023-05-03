import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

class ExploringBTCLowClass:
    def btc_low_price(self,start_date,end_date):
        cryptocurrencies = ['BTC-USD']
        #data = yf.download(cryptocurrencies,start='2020-01-01', end='2022-08-31')
        data = yf.download(cryptocurrencies, start=start_date, end=end_date)
        data["Date"] = data.index
        data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]

        sns.set_theme(style="darkgrid")

        data['Date'] = pd.to_datetime(data['Date'])
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        #plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=300))
        #plt.xticks(rotation = 45, ha = 'right')
        sns.lineplot(x = "Date", y = "Low", data = data)
        plt.title('BTC Low Price', fontsize=20, color='green')
        plt.xlabel("Low Price Dates", fontsize=17, color='blue')
        plt.ylabel("Low Price($)", fontsize=17, color='blue')
        fig = plt.gcf()
        fig.canvas.set_window_title('BTC-Low Price')
        plt.show()
