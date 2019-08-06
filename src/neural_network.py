import dataDescription as dd

import pandas as pd

from sklearn.linear_model import Perceptron
from sklearn.preprocessing import normalize

# return neural network mode
def get_model(data):
    x_train = data.loc[:, data.columns != 'SalePrice']
    x_train = normalize(x_train)
    y_train = data['SalePrice']
    perc = Perceptron()
    perc.fit(x_train, y_train)

    return perc

# get predictions with neural network model (perceptron)
def predict_output(perc, x_test):
    x_test = normalize(x_test)
    predict = perc.predict(x_test)
    return predict



# get predictions and save it to the datafram
def main():
    df_train, id_col_train = dd.get_train_dataframe() # train dataset
    df_to_predict, id_col_predict = dd.get_test_dataframe() # dataset to predict results
    perc = get_model(df_train)
    prediction = predict_output(perc, df_to_predict)

    df_out = pd.DataFrame(columns=['Id', 'SalePrice'])
    df_out['Id'] = id_col_predict['Id']
    df_out['SalePrice'] = prediction
    return df_out

df_out = main()
df_out.to_csv("submission_nn.csv", index=False)