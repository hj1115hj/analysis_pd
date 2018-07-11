from datetime import datetime
                 #시간대 변경
                #datetime 패키지고 timedelta는 함수다.
from .api import api

import json
import math


def preprocess_post(data):      #data 전처리 적재하기전의 과정
    del data['addrCd']
    del data['rnum']

    data['count_locals'] = data['csNatCnt']
    del data['csNatCnt']

    data['count_foreigner'] = data['csForCnt']
    del data['csForCnt']

    data['tourist_spot'] = data['resNm']
    del data['resNm']

    data['restrict1'] = data['sido']
    del data['sido']

    data['restrict2'] = data['gungu']
    del data['gungu']

    data['date']=data['ym']
    del data['ym']







def crawling_tourspot_visitor(district, start_year, end_year, fetch =True,
                               result_directory = '',service_key=''):

    #서울특별시_tourinstspot_2017_2017.json
    filename = '%s/%s_tourinstspot_%s_%s.json' % (result_directory, district,start_year,end_year)

    result_list = []
    results=[]

    if fetch is True:
    #해당검색어에대한 모든 페이지를 검색한다
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                result_list =api.pd_fetch_tourspot_visitor(district1=district,year= year,month= month, numofrow=10, pageno = 1,
                                                           service_key=service_key)#2017 년 1,2,3,4,5,6~12월pageNo=1 , row 10
                for data in result_list:
                    print(data)
                    preprocess_post(data)
                    results.append(data)


        # save data to file

        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename




def preprocess_foreign_visitor(data):
    # ed
    del data['ed']

    # edCd
    del data['edCd']

    # rnum
    del data['rnum']

    #나라 코드
    data['country_code'] = data['natCd']
    del data['natCd']

    #나라 이름
    data['country_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    #방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년월
    if 'ym' not in data:
        data['date'] = ''
    else:
        data['date'] = data['ym']
        del data['ym']



def crawling_foreign_visitor(country, start_year, end_year,fetch=True,result_directory='',
                             service_key=''):
    results = []

    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (
        result_directory, country[0], country[1], start_year, end_year)

    for year in range(start_year, end_year+1):
        for month in range(1, 13):

            data = api.pd_fetch_foreign_visitor(country[1], year, month, service_key)
            if data is None:
                continue


            preprocess_foreign_visitor(data)
            results.append(data)

    # save data to file


    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename

