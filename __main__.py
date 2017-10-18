from config import CONFIG
import collection
import analyze
import visualize

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    resultfiles = dict()

    # collection
    resultfiles['tourspot_visitor'] = collection.crawling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        resultfiles['foreign_visitor'].append(collection.crawling_foreign_visitor(country, **CONFIG['common']))

    # 1. analysis & vsualization
    # result_analysis = analyze.anlysis_correlation(resultfiles)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis & vsualization
    result_analysis = analyze.anlysis_correlation_by_tourspot(resultfiles)

    r_table = pd.DataFrame(result_analysis, columns=('tourspot', 'r_일본', 'r_미국', 'r_중국'))
    print(r_table)
    r_table = r_table.set_index('tourspot')
    #r_table = r_table.drop('서울시립미술관 본관')
    #r_table = r_table.drop('서대문자연사박물관')

    r_table.plot(kind='bar', rot=70)
    plt.show()