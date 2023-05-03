# Multiple linear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import seaborn as sns
# importing r2_score module
from sklearn.metrics import r2_score

class PredictingBTCVolumeClass:
    def predict_btc_volume_price(self, pred_date):
        cryptocurrency = ['BTC-USD']
        data = yf.download(cryptocurrency)
        data["Date"] = data.index
        data = data[["Date", "Volume"]]
        # Convert "Fee" from int to string
        data = data.astype({'Date': 'string'})
        print(data.dtypes)

        splited = data['Date'].str.split('-', expand=True)
        data['year'] = splited[0].astype('int')
        data['month'] = splited[1].astype('int')
        data['day'] = splited[2].astype('int')

        for k in data.index:
            if data.loc[k, "Volume"] > 250000000:
                data.drop(k, inplace=True)

        sns.boxplot(data["Volume"])
        plt.show()

        print("---------types----------")
        print(data.dtypes)
        print(data.tail())
        # Extracting Independent and dependent Variable
        X = data.iloc[:, 2:5].values
        y = data.iloc[:, 1].values

        print("----------------------")

        df1 = pd.DataFrame(X)
        #print("X Data")
        # print(df1)
        df2 = pd.DataFrame(y)
        #print("Y Data")
        # print(df2)

        print("-----------prediction-------------")
        # Execute the following code to divide our data into training and test sets:
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        # Load linear regression class
        from sklearn.linear_model import LinearRegression
        # creating an instance of liner regression
        regressor = LinearRegression()
        # fittig data
        regressor.fit(X_train, y_train)
        # Making Predictions
        y_pred = regressor.predict(X_test)
        # To compare the actual output values for X_test with the predicted value
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        #print(df.to_string())

        # predicting the accuracy score
        score = r2_score(y_test, y_pred)
        print("Volume-r2 socre is ", score * 100)

        #dt = [[2023, 12, 30]]
        #new_pred = regressor.predict(dt)
        new_pred = regressor.predict(pred_date)

        print(new_pred)

        print("--------------------")

#ob=PredictingBTCOpenClass()
#dt = [[2025, 12, 30]]
#ob.predict_btc_open_price(dt)







