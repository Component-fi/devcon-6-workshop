from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


def process_data(prices):
    train_amount = int(0.8*len(prices))
    train = prices.iloc[0:train_amount]
    test = prices.iloc[train_amount:]

    plt.plot(train, color = "black")
    plt.plot(test, color = "red")
    plt.ylabel('ETH Price')
    plt.xlabel('Datetime')
    plt.title("Train/Test split for ETH Data")
    plt.show()

    y = train['price']
    ARMAmodel = SARIMAX(y, order = (1, 0, 1))
    ARMAmodel = ARMAmodel.fit()
    y_pred = ARMAmodel.get_forecast(len(test.index))
    y_pred_df = y_pred.conf_int(alpha = 0.05) 
    y_pred_df
    y_pred_df["Predictions"] = ARMAmodel.predict(start = y_pred_df.index[0], end = y_pred_df.index[-1])
    y_pred_df.index = test.index
    y_pred_out = y_pred_df["Predictions"]

    plt.plot(y_pred_out, color='green', label = 'Predictions')
    plt.legend()
    print(y_pred_out)

    import numpy as np
    from sklearn.metrics import mean_squared_error

    arma_rmse = np.sqrt(mean_squared_error(test["price"].values, y_pred_df["Predictions"]))
    print("RMSE: ",arma_rmse)

    # now we need to interpet this as a long or short
    if y_pred_out[0] > y_pred_out.iloc[-1]:
        return False