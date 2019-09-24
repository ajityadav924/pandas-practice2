import pandas as pd
df=pd.read_csv("Housing.csv")
#print(df)
print(df.head())                          #to print 1^st 5 rows
print(df.tail())                          #to print last 5 rows
print(df[20:30])                           #to print the rows between 20 to 30
print(df.dtypes)
print(df['bedrooms'].describe())
print(df['price'].mean())
print(df['price'].head(50).mean())
print(df['price'].mean())
print(df[['lotsize','price','bedrooms']])
print(df.groupby('bedrooms')[['price']].mean())
a=df.groupby('bedrooms').mean()
print(a)
df_sub=df[df['lotsize']<6000]
print(df_sub.mean())
