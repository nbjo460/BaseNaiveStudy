import pandas as pd
df = pd.read_csv("../csv/titanic.csv")
print(df)
print(df["Survived"].value_counts(normalize=True))