import numpy as np
import pandas as pd


df1=pd.DataFrame(   [ {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 30, 'phone': '010-2222-2222'},
    {'name': '도우넛', 'age': 20, 'phone': '010-3333-3333'}])
print(df1)
df = pd.DataFrame({'A' : [5,6,3,4], 'B' : [1,2,3, 5]})
print(df)
print(df[df['A'] == 3])
for row in df.itertuples():
    print ("A :",row.A,"B :",row.B)

for row in df1.itertuples():
    print ("name :",row.name,"age :",row.age)

