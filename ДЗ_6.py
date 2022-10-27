import pandas as pd
f = pd.read_csv("telecom_churn.csv")
#Упражнение 3
x = f["Total day calls"].mean()
print(x)
#Упражнение 4
print(f[f.State=='AK']['Total day calls'].mean())
#Упражнение 5
y = f.groupby(["State"]).agg({"Total day calls": "mean"})
print(y)
#Упражнение 6
print(y[y['Total day calls']>x])
#Упражнение 7
a=f.groupby(['State']).agg({'Total day calls':'mean','Total eve calls':'mean'})
print(a)
#Упражнение 8
a['answer']=a['Total day calls']>a['Total eve calls']
print(a)
#Упражнение 9
print((f['International plan']=='Yes').sum()/3333)
print((f['Voice mail plan']=='Yes').sum()/3333)
#Упражнение 10
print(f['Area code'].nunique())
#Упражнение 11
a = f.groupby('Customer service calls').agg({'State':'count'})
print(a)
#Упражнение 13
print(f['Total intl calls'].mean())
#Упражнение 15
a = f.groupby('Churn').agg({'Total day charge':'sum'})
print(a)
#Упражнение 16
print(f.groupby(['State']).agg({'Total day charge':'mean'}).sort_values(by='Total day charge'))
#Упражнение 17
print(f.groupby('Area code').mean())
#Упражнение 18
print(f.loc[[100, 102, 104], ['State', 'Churn']])
#Упражнение 18
data = {'A': [1, 2, 3, 4, 5, 6, 7],'B': [9, 8, 7, 6, 7, 8, 9]}
f = pd.DataFrame(data)
df = f['A']**2 + f['B']**2
f['сумма квадратов'] = df
print(f)
#Упражнение 19
df2 = f.apply(lambda x: x[:3].mean(), axis=1)
f['среднее значение'] = df2
print(f)