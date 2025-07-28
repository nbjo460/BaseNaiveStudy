import pandas as pd
df = pd.read_excel("../excell/all.xlsx")
df = df.drop(index=[0,1], axis = 0)
df.columns = df.iloc[0]
df = df.drop(index=2, axis = 0)

df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')

df = df.reset_index(drop=True)
print(df.columns)
print(df[(df["קטגוריה"]=="מזון וצריכה") & (df["שם בית העסק"]!="ימא זול")].groupby(by="שם בית העסק", as_index=True).agg({"סכום חיוב":"sum"}).sort_values("סכום חיוב"))
