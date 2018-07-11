# facebook api Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request
from datetime import datetime
import math

'''
서비스키를 params 로 주면 안되는이유.
중간중간 52가 자꾸들어감.. 

'''
#SERVICE_KEY = '10wfesCEKZKTWb9IhpFWutS0D6Z6p2M1j9BlDf0VCuhfzvsI74IuQND3AgnhxdIpSyI9lER%2FH55iva04jaZEtA%3D%3D'


def print_json(output):
    return output

def pd_gen_url(endpoint, service_key='', **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param),service_key)
    return url

#for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
 #   print(items)
def pd_fetch_foreign_visitor(country_code, year, month, service_key=''):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(endpoint,
                     service_key,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     NAT_CD= country_code,
                     ED_CD = 'E',
                     _type ='json')

    json_result = json_request(url=url,success=print_json)
    #print(json_result)
    json_response = json_result.get('response')
    #print(json_response)
    json_header = json_response.get('header')

    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' %(datetime.now(),result_message,url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0,numofrow=10, pageno=1,
                              service_key=''):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    result_list = []
    hasnext = True
    flag = True

    while hasnext:
        url = pd_gen_url(
            endpoint=endpoint,
            service_key=service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=numofrow,
            _type='json',
            pageNo=pageno)   # 2017 년 1,2,3,4,5,6~12월pageNo=1 , row 10
        json_result = json_request(url=url)
        json_body = json_result.get('response').get('body')

        data_list = json_body.get('items').get('item')
        if flag:
            numofrows = json_body.get('numOfRows')
            totalcount = json_body.get('totalCount')
            last_page = math.ceil(totalcount / numofrows)
            flag = False

        for data in data_list:
            if data is None:
                continue

            result_list.append(data)

        if pageno == last_page:
            hasnext = False
        else:
            pageno = pageno + 1
    return result_list


'''
#페이지 의사코드
+
+    pageno = 1
+    hasnext = True
+
+    while hasnext:
+        url = pd_gen_url(...... , numOfRows=50, pageNo=pageno)
+        json_result = json_request(url=url)
+
+
+        json_body = json_response.get('body')
+        numofrows = json_body.get('numOfRows')
+        totalcount = json_body.get('totalCount')
+
+        if totalcount == 0:
+            break
+
+        last_page = math.ceil(totalcount/numofrows)
+        if pageno == last_page:
+            hasnext = False
+        else:
+            pageno += 1
+

'''

'''
def pd_fetch_posts(pagename, since, until):
    url = pd_gen_url(node=pd_name_to_id(pagename) + "/posts",
                     fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
                     since=since,
                     until=until,
                     limit=50,
                     access_token=ACCESS_TOKEN)

    # results = [] # yield로 대체
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')
        # results += posts
        # results.append(posts)
        url = None if paging is None else paging.get("next")
        isnext = url is not None

        yield posts


'''

