from collect.api import api

'''
id = api.fb_name_to_id("jtbcnews")
print(id)

'''


'''
# test for pd_gen_url
url = api.pd_gen_url(
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)

print('print url')
print(url)


'''

'''
#Test for foreign__visitor pd_gen_url
endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
url = api.pd_gen_url(endpoint,
                     YM='{0:04d}{1:02d}'.format(2012, 7),
                     NAT_CD= 112,
                     ED_CD = 'E',
                     _type ='json')
print(url)


'''

#Test for pd_fetch_foreign__visitor
#body.response.items.item 출력
'''
item = api.pd_fetch_foreign_visitor(112,2012,7)
print(item)

'''

'''
for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
    print(items)

'''


