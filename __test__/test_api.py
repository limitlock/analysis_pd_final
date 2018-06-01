from collection.api import pd_gen_url, pd_fetch_tourspot_visitor, pd_fetch_foreign_visitor

# test for pd_gen_url
'''
url = pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    service_key=SERVICE_KEY,
    YM='{0:04d}{1:02d}'.format(2012, 1),
    SIDO='부산광역시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)

print(url)
'''

# test for pd_fetch_foreign_visitor
#item = pd_fetch_foreign_visitor(112, 2017, 11)
#print(item)


# test for pd_fetch_tourspot_visitor
for item in pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=1):
   print(item)

