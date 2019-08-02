from reader import Reader as r


def create_unique_dict(data):
    key = 1
    dict = {}
    for i in data:
        if i not in dict.keys():
            dict[i] = key
            key += 1
    return dict


def map_data(data):
    # drop index
    data.drop(['Id'], axis=1, inplace=True)

    # iterate each column
    for column in data.columns:
        enum_type = False
        # check if columns has numbers of some enum values
        for val in data[column]:
            if type(val) != int and type(val) != float:
                enum_type = True
                break;

        # if in column are enum type values, create unique dict with int indexes and map values to int
        if enum_type:
            unique_dict = create_unique_dict(data[column])
            new_column_vals = []
            # map all values
            for val in data[column]:
                new_column_vals.append(unique_dict[val])
            # change whole column to new mapped values
            data[column] = new_column_vals

    return data


# data = r('train.csv', 'data').csv_to_df()
# print(data)
# print(map_data(data))