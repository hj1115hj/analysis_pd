import json
import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math
import os

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r

def analysis_correlation1(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())

    # csv/excel 파일로 저장해보기
    if not os.path.exists('__results__/file'):
        os.makedirs('__results__/file')
    #filename = '__results__/file/_tourspotvisitor_table.csv';
    # with open(filename, 'w', encoding='utf-8') as outfile:
    #     outfile.write(tourspotvisitor_table.to_excel())
    #tourspotvisitor_table.to_csv(filename, mode='w')
    filename = '__results__/file/tourspotvisitor_table.xlsx'
    writer = pd.ExcelWriter(filename)
    tourspotvisitor_table.to_excel(writer,'tourspotvisitor_table')
    temp_tourspotvisitor_table.to_excel(writer,'temp_tourspotvisitor_table')
    writer.save()
    #df.to_excel('foo.xlsx', sheet_name='sheet1')


    results = []
    filename = '__results__/file/foreignvisitor_table.xlsx'
    writer = pd.ExcelWriter(filename)
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        #print(foreignvisitor_table)

        foreignvisitor_table = foreignvisitor_table.set_index('date')
        merge_table = pd.merge(
            temp_tourspotvisitor_table,
            foreignvisitor_table,
            right_index=True,
            left_index=True
            ) # index 조건으로 합치지않으면, -> 여기는 rownuwm 인덱스가 명시된것이아니기때문에 다른 컬럼의 공통속성을 가지고
        #merge를 수행하는데 공통속성이 없으므로 에러가난다. 만드시 right_index와 left_index를 명시해주자

        x = list(merge_table['visit_count']) # 해당 년,월,일 나라방문객수
        y = list(merge_table['count_foreigner']) #해당 년,월, 일  한국 방문객수
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        r = ss.pearsonr(x, y)
        #r = ss.pearsonr(x, y)[0]
        #r = np.corrcoef(x, y)[0]
        print({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})

        #merge_table['visit_count'].plot(kind='bar')
        #plt.show()

        # excel 파일로 저장해보기
        sheet_name1 = '%s_foreignvisitor_table' %(country_name)
        sheet_name2 = '%s_merge_table' %(country_name)
        foreignvisitor_table.to_excel(writer, sheet_name1)
        merge_table.to_excel(writer, sheet_name2)
    writer.save()


    return results


def analysis_correlation2(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        #print(foreignvisitor_table)

        foreignvisitor_table = foreignvisitor_table.set_index('date')
        merge_table = pd.merge(
            temp_tourspotvisitor_table,
            foreignvisitor_table,
            left_index = True, right_index = True)

        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        r = ss.pearsonr(x, y)[0]
        #r = np.corrcoef(x, y)[0]
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        merge_table['visit_count'].plot(kind='bar') # datafram의 index값을 x축으로 ,y축을 visit_count로 해서 그린다.
        plt.show()
    return results


def analysis_correlation_by_tourspot(resultfiles):


    #날짜에 따른 나라별 한국 방문객수

    foreignvisitor_table = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        temp = pd.DataFrame(json_data, columns=['date', 'visit_count','country_name'])
        new_name = temp['country_name'].unique().item(0)
        #print(new_name)
        temp.rename(columns=lambda x: x.replace('visit_count',new_name ), inplace=True)
        del temp['country_name']

        foreignvisitor_table.append(temp.set_index('date'))

    merge_table = pd.merge(foreignvisitor_table[0], foreignvisitor_table[1], left_index=True, right_index=True)
    merge_table = pd.merge(merge_table, foreignvisitor_table[2], left_index=True, right_index=True)


    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])
    tourist_spot = tourspotvisitor_table['tourist_spot'].unique()

    print(merge_table)

    # 날짜에 따른 관광지별 한국 방문객수&& 파일로 저장
    filename = '__results__/file/merge_table.xlsx'
    writer = pd.ExcelWriter(filename)
    r_list =[]
    #graph_table = pd.DataFrame(result_analysis, colums=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    for i, spot in enumerate(tourist_spot):
        temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == spot]
        temp_table = temp_table.set_index('date')
        result_table = pd.merge(temp_table, merge_table, left_index=True, right_index=True)
        #print(result_table)
        #날짜에따른 각 관광지마다 의 방문계수와 나라별 한국 방문개수의 상관 계수를 구한다
        temp_list = []
        temp_list.append(spot)
        #print(spot)
        for col in list(result_table.columns):

            if col == 'count_foreigner' or col == 'tourist_spot' :
                continue
            #print(col)
            #print(list(result_table['count_foreigner']))
            #print(list(result_table[col]))
            #print(correlation_coefficient(list(result_table['count_foreigner']), list(result_table[col])))

            temp_list.append(
                correlation_coefficient(
                    list(result_table[col]),
                    list(result_table['count_foreigner']) ))
        result_table.to_excel(writer,'result_table_%d' % i)

        r_list.append(temp_list)
    writer.save()
    return r_list

