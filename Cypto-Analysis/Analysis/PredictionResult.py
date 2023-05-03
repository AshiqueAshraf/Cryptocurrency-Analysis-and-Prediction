import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class PredictionResultClass:
    def plot_prediction(self,price,date,crypt,status):
        self.crypt=crypt
        self.date=date
        self.title=status
        self.price=price
        #data = {"Currency": ["2022-10-17"], "Price": [21000]}
        data = {"Date": [date], "Price": [price]}
        df = pd.DataFrame(data, columns=['Date', 'Price'])
        plt.figure(figsize=(5, 5))
        plots = sns.barplot(x="Date", y="Price", data=df)
        for bar in plots.patches:
            plots.annotate(format(bar.get_height(), '.2f'),
                   (bar.get_x() + bar.get_width() / 5,
                    bar.get_height()), ha='center', va='center',
                   size=15, xytext=(0, 5),
                   textcoords='offset points')
        tit=    "Predicted"+" " +self.crypt +" "+self.title+" "+"Price"
        plt.title(tit)
        fig = plt.gcf()
        fig.canvas.set_window_title(tit)
        plt.show()

#data = {"Currency": ["2022-10-17"], "Price": [21000]}
#price=21000
#dats="2022-10-17"
#cry="BTC"
#stat="Open"
#ob=PredictionResultClass()
#ob.plot_prediction(price,dats,cry,stat)