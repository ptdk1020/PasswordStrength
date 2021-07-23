"""This file extracts interesting info from zxcvbn"""

from zxcvbn import zxcvbn
import pandas as pd

test = pd.DataFrame(['password'], columns=['password'])


def zxcvbn_extract(file, destination):
    df = pd.read_csv(file)
    #df = df['password']
    #df = test

    cols = ['pw', 'english_wikipedia', 'female_names', 'male_names',
            'passwords', 'surnames', 'us_tv_and_film']
    dz = pd.DataFrame(columns=cols)
    for col in dz.columns:
        if col == 'pw':
            dz[col] = df['password']
        else:
            dz[col] = ''


    for index, row in dz.iterrows():
        D = zxcvbn(df.iloc[index, 0])

        for item in D['sequence']:
            if item['pattern'] == 'dictionary':
                try:
                    if row[item['dictionary_name']] == '':
                        row[item['dictionary_name']] = item['matched_word']
                    else:
                        row[item['dictionary_name']] = row[item['dictionary_name']] + ',' + item['matched_word']
                except:
                    pass

    dz.to_csv(destination, index=False)
    print('Done')
    return


file = '../data/kaggle_processed.csv'
destination = '../data/kaggle_zxcvbn.csv'

zxcvbn_extract(file, destination)

