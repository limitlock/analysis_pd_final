import collection
from config import CONFIG

if __name__ == '__main__':

    # collection
    collection.crawling_tourspot_visitor(CONFIG['district'], **CONFIG['common'])

    for country in CONFIG['countries']:
        collection.crawling_foreign_visitor(country, **CONFIG['common'])

    # analysis

    # vsualization
