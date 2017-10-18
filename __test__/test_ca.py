import json
import pandas as pd


with open('../__results__/crawling/서울특별시_tourspot_2017_2017.json', 'r', encoding='utf-8') as infile:
    json_data = json.loads(infile.read())

tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])
temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('date')['count_foreigner'].sum())

with open('../__results__/crawling/중국(112)_foreignvisitor_2017_2017.json', 'r', encoding='utf-8') as infile:
    json_data = json.loads(infile.read())

foreignvisit_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
country_name = foreignvisit_table['country_name'].unique().item(0)
temp_foreignvisit_table = foreignvisit_table[['date', 'visit_count']].set_index('date')


merge_table = pd.merge(temp_tourspot_table, temp_foreignvisit_table, left_index=True, right_index=True)
print(merge_table)

