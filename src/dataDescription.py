from reader import Reader as r
import numpy as np
import math

def create_unique_dict(data):
    key = 1
    dict = {}
    for i in data:
        if i not in dict.keys():
            dict[i] = key
            key += 1
    return dict


def map_data(data):
    # save id column to create submission with pattern - Id, SalePrice
    id_col = data[['Id']]
    # drop index
    data.drop(['Id'], axis=1, inplace=True)

    # iterate each column
    for column in data.columns:
        enum_type = False

        # check if columns has numbers of some enum values
        for val in data[column]:
            if type(val) != int and type(val) != float:
                enum_type = True
                break


        # if in column are enum type values, create unique dict with int indexes and map values to int
        if enum_type:
            unique_dict = create_unique_dict(data[column])
            new_column_vals = []
            # map all values
            for val in data[column]:
                new_column_vals.append(unique_dict[val])
            # change whole column to new mapped values
            data[column] = new_column_vals

    # change all NaN to median of this column
    for column in data.columns:
        if np.isnan(data[column]).any():
            median_val = math.floor(data[column].median())
            new_col = data[column].fillna(median_val)
            data[column] = new_col

    return data, id_col


def get_train_dataframe():
    data = r('train.csv', 'data').csv_to_df()
    return map_data(data)


def get_test_dataframe():
    data = r('test.csv', 'data').csv_to_df()
    return map_data(data)