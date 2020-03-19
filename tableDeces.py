import pandas as pd
import urllib.request


# import csv from web
data = urllib.request.urlopen("https://www.data.gouv.fr/fr/datasets/r/0b66ca39-1623-4d9c-83ad-5434b7f9e2a4")

#  fills a list with csv elements
dataList = []
for item in data:
  dataList.append(item.decode('utf-8').replace("\n",","))

#  list to dataframe
df1 = pd.DataFrame([sub.split(",") for sub in dataList])

# promote headers
headers = df1.iloc[0]
tD = pd.DataFrame(df1.values[1:], columns=headers)
tD = tD.set_index(['date'])

# réduction sur colonnes date maille_code et deces
tD=tD[['maille_code', 'deces']]

# réduction sur les lignes 'FRA'
tDFr = tD[tD.maille_code == 'FRA']

#  tDFr = tDFr.reindex(tDFr.deces.astype(float).index)
tDFr = tDFr.astype({'deces': 'int32'})

tDFr.to_csv('extract.csv')
