import random
import pandas as pd


def aggregator(group):
    print('-------------------------')
    print(group)
    group.iloc[0]['b'] = group.iloc[0]['b'] + 1000
    group.iloc[0]['c'] = group.iloc[0]['c'] + 1000
    group.loc[0, 'd'] = 999
    print(group)
    group.reset_index(drop=True, inplace=True)
    group.iloc[0]['b'] = group.iloc[0]['b'] + 10000
    group.iloc[0]['c'] = group.iloc[0]['c'] + 10000
    group.loc[0, 'd'] = 888
    print(group)
    return group


def test1():
    data = {'a': [], 'b': [], 'c': []}

    i = 0
    while i < 10:
        data['a'].append(round(random.random() * 1, 0))
        data['b'].append(round(random.random() * 100, 0))
        data['c'].append(round(random.random() * 1000, 0))
        i += 1

    #print(data)

    df = pd.DataFrame(data)
    print(df)

    df1 = df.sort_values(by=['a'])
    print(df1)
    df1.reset_index(drop=True, inplace=True)
    print(df1)

    df2 = df.sort_values(by=['b']).groupby('a').apply(aggregator)
    print('==================================')
    print(df2)
    df2.reset_index(drop=True, inplace=True)
    print(df2)

test1()