import pandas as pd

# Series와 dict 데이터를 사용한 DataFrame
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)

# list와 dict를 활용
data = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 30, 'phone': '010-2222-2222'},
    {'name': '도우넛', 'age': 20, 'phone': '010-3333-3333'}
]

print('dict을 이용한 데이터 프레임 만들기------------')
df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(df, columns=['name', 'phone'])
print(df2)

# 데이터 추가 (열 추가)
print('----------데이터 추가--------')
df2['height'] = [150, 160, 170]
print(df2)

# 인덱스 선택
print('-------인덱스 선택 -------')
df3 = df2.set_index('name') #  df2 이름을 인덱스로 하여 df3를 만든다.
print(df3)

# 컬럼 선택
#
print(s, type(s))

# merge
print('---merge---')
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
print(df2)
print(df4)
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)

# merge & join
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희'],
})
print(df1)
#df1=df1.set_index('고객번호')
#print(df1)
df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

print(df2)
#df2 = df2.set_index('고객번호')
#print(df2)
# 공통 열인 고객번호를 기준으로 테이터를 찾아서 합친다.
# 이 때, 기본적으로 양쪽 데이터프레임에 모두 키가 존재하는
# 데이터만 합쳐진다(inner join 방식)
print('-----df3------')
df3 = pd.merge(df1, df2, left_index=True, right_index=True) #그냥합치면 인덱스가 가닌 공통열로 합쳐진다.

print(df3)


# outer join 방식은 키값이 한쪽에만 있어도 양쪽 데이터를 모두
# 합쳐진다.(full)
print('---------check------')
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# left, 첫 번째 파라미터의 데이터프레임의
# 데이터를 전부 합치는 방식
# 첫번째 파라미터가 없어도 다보여주고 왼쪽값은 Nan으로 표시
print('-------left----------')
df3 = pd.merge(df1, df2, how='left')
print(df3)

# right, 두 번째 파라미터의 데이터프레임의
# 데이터를 전부 합치는 방식
print('-------right ---------')
df3 = pd.merge(df1, df2, how='right')
print(df3)


# 기준열은 on 인수로 명시적 설정이 가능하다.
# 겹치는거 다 뽑느다. 기분지 없으니깐.
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

print('-----------df1')
print(df1)

print('-----------df2')
print(df2)
df3 = pd.merge(df1,df2, left_index=True , right_index= True)
print('---------check-----index_left, right true----')
print(df3)
df3 = pd.merge(df1, df2)
print('---------check-----------')
print(df3)

df3 = pd.merge(df1, df2, on=['성별', '연령'])
print(df3)


df3 = pd.merge(df1, df2, on=['성별'])
print(df3)

