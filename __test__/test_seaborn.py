import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

with open('../__results__/crawling/중국(112)_foreignvisitor_2011_2017.json', 'r', encoding='utf-8') as infile:
    json_data = json.loads(infile.read())

cn_visit_table = pd.DataFrame(json_data, columns=['date', 'visit_count'])
cn_visit_table.date = pd.to_datetime(cn_visit_table.date, format='%Y%m')
cn_visit_table['year'] = cn_visit_table.date.dt.year
cn_visit_table['month'] = cn_visit_table.date.dt.month

cn_visit_table = cn_visit_table.set_index(['month', 'year'])['visit_count'].unstack(fill_value=0)
sb.heatmap(cn_visit_table)
plt.show()