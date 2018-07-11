import os

# configuration
CONFIG = {
    'district': '서울특별시',
    'countries': [('중국', 112), ('일본', 130), ('미국', 275)],
    'f_service_key' :'sTXgOSK68LSPXZXHeK%2BmsGS6z7fCMvv21Tg5CNe%2FiLrqwmkxranNOBROIG5FYsuNklbb7EVuePlb%2BIe42f2qDA%3D%3D',
    't_service_key' :'sTXgOSK68LSPXZXHeK%2BmsGS6z7fCMvv21Tg5CNe%2FiLrqwmkxranNOBROIG5FYsuNklbb7EVuePlb%2BIe42f2qDA%3D%3D',
    'common': {
        'start_year': 2017,
        'end_year': 2017,
        'fetch': True,
        'result_directory': '__results__/crawling'

    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])