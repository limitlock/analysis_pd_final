from .json_request import json_request
from urllib.parse import urlencode
from itertools import count

SERVICE_KEY = 'xndt9aE0vWNU2zQcWp8iBPms%2BTgWggyBYGwQkxs47RHcSdy12U%2FpUDZ7dS4TT33OLafiai%2By6fiCNqdkEwnkWA%3D%3D'
NUM = 100


def pd_gen_url(endpoint, service_key, **params):
    return '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), service_key)


# 출입국관광통계조회
def pd_fetch_foreign_visitor(
        country_code=0,  # 나라코드
        year=0,
        month=0,
        service_key=SERVICE_KEY):
     url =  pd_gen_url(
        endpoint='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
        service_key=service_key,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        _type='json'
     )
     print(url)
     json_result = json_request(url=url)
     json_response = None if json_result is None else json_result.get('response')
     json_body = None if json_response is None else json_response.get('body')
     json_items = None if json_body is None else json_body.get('items')
     json_in_item = None if json_items is None else json_items.get('item')
     return json_in_item







# 유료 관광지 방문객수 조회
def pd_fetch_tourspot_visitor(
        district1='', #시도
        district2='', #시군구 (생략가능)
        tourspot='', # 관광명소
        year=0,
        month=0,
        service_key=SERVICE_KEY):

        url = pd_gen_url(
            'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
            service_key=service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=10,
            _type='json',
            pageNo=1)

        isnext = True

        while isnext is True:
            json_result = json_request(url=url)

            json_response = None if json_result is None else json_result.get('response')
            json_message = None if json_response is None else json_response.get('resultMsg')
            json_body = None if json_response is None else json_response.get('body')
            json_items = None if json_body is None else json_body.get('items')
            json_in_item = None if json_items is None else json_items.get('item')
            if 'OK' != json_message:
                isnext = False

            yield json_in_item