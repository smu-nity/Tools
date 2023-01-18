import pandas as pd

df = pd.read_excel('data.xlsx')

for _, item in df.iterrows():
    if item[0].isnumeric():
        print(item[0])
        print(item[1])
        print(item[2])
        print(item[6])
        print(item[7])
        print(item[19])
