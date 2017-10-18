import json

import math
import pandas as pd


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


def anlysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])

    tourspots = tourspot_table['tourist_spot'].unique()

    results = []
    for tourspot in tourspots:
        temp_table = tourspot_table[tourspot_table['tourist_spot'] == tourspot].set_index('date')

        data = {'tourspot': tourspot}

        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())

            foreignvisit_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            country_name = foreignvisit_table['country_name'].unique().item(0)
            temp_foreignvisit_table = foreignvisit_table[['date', 'visit_count']].set_index('date')

            merge_table = pd.merge(temp_table, temp_foreignvisit_table, left_index=True, right_index=True)

            x = list(merge_table['visit_count'])
            y = list(merge_table['count_foreigner'])
            data['r_' + country_name] = correlation_coefficient(x, y)

        results.append(data)

    return results




def anlysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])
    temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('date')['count_foreigner'].sum())

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisit_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        country_name = foreignvisit_table['country_name'].unique().item(0)
        temp_foreignvisit_table = foreignvisit_table[['date', 'visit_count']].set_index('date')

        merge_table = pd.merge(temp_tourspot_table, temp_foreignvisit_table, left_index=True, right_index=True)

        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        r = correlation_coefficient(x, y)
        results.append({'country_name': country_name, 'r': r, 'x': x, 'y': y})

    return results




