import pandas as pd
df = pd.DataFrame()
df["color"] = ['blue', 'red','yellow', 'green']
df["radius"]=[2,4,3,5]
df['diameter'] = df['radius']*2
print(df)
print(df['diameter'].sum())
print(df['radius'].mean())
print(df['radius'].min())

df['age']= [5,8,7,7]
df['name']=['f', 's','g','h']
print(df.iloc[-1])# տպում է բոլոր տողերի վերջին էլեմենտները