from collection.api import pd_fetch_tourspot_visitor, pd_fetch_foreign_visitor
import json
import os

RESULT_DIRECTORY = '__results__/crawling'

# 유료 관광지 방문객수 조회
def preprocess_tourspot_visitor(item):
    if 'addrCd' in item:
        del item['addrCd']

    if 'rnum' in item:
        del item['rnum']

    #내국인 = csNatCnt
    if 'csNatCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
        del item['csNatCnt']

    # 외국인 =csForCnt
    if 'csForCnt' not in item:
        item['count_forigner'] = 0
    else:
        item['count_forigner'] = item['csForCnt']
        del item['csForCnt']

    #관광명소
    if 'resNm' not in item:
        item['tourist_spot'] = 0
    else:
        item['tourist_spot'] = item['resNm']
        del item['resNm']

    #날짜
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
        del item['ym']

    #시
    if 'sido' not in item:
        item['restrict1'] = 0
    else:
        item['restrict1'] = item['sido']
        del item['sido']

    #시군구
    if 'gungu' not in item:
        item['restrict2'] = 0
    else:
        item['restrict2'] = item['gungu']
        del item['gungu']


# 출입국관광통계조회
def preprocess_foreign_visitor(item):
    #나라코드 = natCd
    if 'natCd' not in item:
        item['country_code'] = 0
    else:
        item['contry_code'] = item['natCd']
        del item['natCd']

    #나라명 = natKorNm
    if 'natKorNm' not in item:
        item['country_name'] = 0
    else:
        item['contry_name'] = item['natKorNm']
        del item['natKorNm']
    #날짜 = ym
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
        del item['ym']
    #출입국자 = num
    if 'num' not in item:
        item['visit_count'] = 0
    else:
        item['viswit_count'] = item['num']
        del item['num']

    if 'ed' in item:
        del item['ed']

    if 'edCd' in item:
        del item['edCd']

    if 'rnum' in item:
        del item['rnum']

# 출입국관광통계조회
def crawling_foreign_visitor(
        country,
        start_year,
        end_year):
    results = []
    filename = '%s/%s_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country, start_year, end_year)

    start_year = str(start_year) + '01'
    end_year = str(end_year) + '13'
    for index in range(int(start_year), int(end_year)):
        item = pd_fetch_foreign_visitor(country_code=country[1], year=int(str(index)[0:4]), month=int(str(index)[4:6]))
        preprocess_foreign_visitor(item)
        results.append(item)

    # save results to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename



#   YM='{0:04d}{1:02d}'.format(year, month),
# 유료 관광지 방문객수 조회
def crawling_tourspot_visitor(
        district,
        start_year,
        end_year):

    results = []
    filename = '%s/%s_tourinstspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)

    start_year = str(start_year) + '01'
    end_year = str(end_year) + '13'

    for index in range(int(start_year), int(end_year)):
        print(str(index)[0:4], str(index)[4:6])
        for items in pd_fetch_tourspot_visitor(district1=district, year=int(str(index)[0:4]), month=int(str(index)[4:6])):
            for item in items:
                preprocess_tourspot_visitor(item)
        results += items

    #print(results)

    # save results to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)