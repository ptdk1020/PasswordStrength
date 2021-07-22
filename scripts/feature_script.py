"""This file contains scripts to add more features to the dataset"""

import feature_maps
import pandas as pd
from inspect import getmembers, isfunction

# a list of pairs (function_name, function) from feature_maps
functions = getmembers(feature_maps, isfunction)


def add_features(df, filename):
    for pair in functions:
        if pair[0] not in df.columns:
            df[pair[0]] = df.apply(lambda row: pair[1](row.password), axis=1)
        print(pair[0] + ' done!')
    df.to_csv(filename, index=False)
    print('Finished!')
    return


frame = pd.read_csv('../data/rockyou_processed.csv')
file = '../data/rockyou_processed.csv'

add_features(frame, file)






