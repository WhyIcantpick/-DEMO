import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
print('___________')

df.dropna()

print(df.head())
print(df.info())

#df["Year"].value_counts().plot(kind = "barh", figsize=(8, 5), grid=True)
#plt.show()

#df["Rating"].plot(kind="hist")
#plt.show()

df.plot(x = "Runtime (Minutes)", y = "Revenue (Millions)", kind="scatter")
plt.show()