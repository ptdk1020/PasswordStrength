"""This file extracts interesting info from zxcvbn"""

from zxcvbn import zxcvbn
import pandas as pd

#test = pd.DataFrame(['password'], columns=['password'])


def zxcvbn_extract(file, destination):
    df = pd.read_csv(file)
    df = pd.DataFrame(df.password)
    df.dropna(inplace=True)

    #df = test
    #df=df.iloc[1000000:2000000, :]

    # create empty dataframe dz
    cols = ['pw', 'words']
    dz = pd.DataFrame(columns=cols, index=df.index)
    for col in dz.columns:
        if col == 'pw':
            dz[col] = df['password']
        else:
            dz[col] = ''

    # use zxcvbn, if a word in a dictionary is detected: <word>,dictionary,bool(l33t),bool(reversed)
    for id, row in dz.iterrows():
        D = zxcvbn(df.loc[id, 'password'])
        for item in D['sequence']:
            try:
                if row['words'] == '':
                    row['words'] = item['matched_word'] + ',' + item['dictionary_name'] + ',' + \
                                   str(item['l33t']) + ',' + str(item['reversed'])
                else:
                    row['words'] += ';' + item['matched_word'] + ',' + item['dictionary_name'] \
                                    + ',' + str(item['l33t']) + ',' + str(item['reversed'])
            except:
                pass

    dz.to_csv(destination, index=False)
    print('Done')
    return


file = '../data/dataset/BTC1.csv'
destination = '../data/dataset_zxcvbn/BTC1_zxcvbn.csv'

zxcvbn_extract(file, destination)

