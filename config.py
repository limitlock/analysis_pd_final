import os

# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'service_key': 'JBCg7boYZcVy3tAfUMWwatEssm05h%2FgZMrqyqRV7a0KGlSI16ST%2BdSZaUVMWH98%2BZ%2BTqfRtU2qXiMNOmZDsGLQ%3D%3D',
        # 'service_key': '%2FfZdR%2Bue1CSxLEnMkZXa9iDYontLTMTIteD5%2BzYCiMYpDKUZNUh2FHGDQ04zazSEmLl34FClDQk8a7flFCIQKA%3D%3D',
        'start_year': 2011,
        'end_year': 2017,
        'restore_directory': '__results__/crawling',
        'fetch': False}}


if not os.path.exists(CONFIG['common']['restore_directory']):
    os.makedirs(CONFIG['common']['restore_directory'])
