from datetime import datetime, timedelta

REF_TITLE_TEST = [
    {'id': 1,
     'name': 'ref_test1',
     'short_name': 'first',
     'description': 'first test reference db'
     },
    {'id': 2,
     'name': 'ref_test2',
     'short_name': 'second',
     'description': 'second test reference db'
     },
    {'id': 3,
     'name': 'ref_test3',
     'short_name': 'third',
     'description': 'third test reference db'
     },
    {'id': 4,
     'name': 'ref_test4',
     'short_name': 'forth',
     'description': 'forth test reference db'
     },
    {'id': 5,
     'name': 'ref_test5',
     'short_name': 'firth',
     'description': 'firth test reference db'
     },
    {'id': 6,
     'name': 'ref_test6',
     'short_name': 'sixth',
     'description': 'sixth test reference db'
     },
    {'id': 7,
     'name': 'ref_test7',
     'short_name': 'seven',
     'description': 'seventh test reference db'
     },
    {'id': 8,
     'name': 'ref_test8',
     'short_name': 'eight',
     'description': 'eight test reference db'
     },
    {'id': 9,
     'name': 'ref_test9',
     'short_name': 'nine',
     'description': 'nineth test reference db'
     },
    {'id': 10,
     'name': 'ref_test10',
     'short_name': 'ten',
     'description': 'tenth test reference db'
     },
    {'id': 11,
     'name': 'ref_test11',
     'short_name': 'eleven',
     'description': 'eleventh test reference db'
     },
]

REF_VERSIONS_TEST_CURRENT = [
    {
        'id': 1,
        'reference_id': 1,
        'version': 'test_1',
        'init_date': datetime.date(datetime.now())
    },
    {
        'id': 2,
        'reference_id': 2,
        'version': 'test_2',
        'init_date': datetime.date(datetime.now())
    },
    {
        'id': 3,
        'reference_id': 3,
        'version': 'test_3',
        'init_date': datetime.date(datetime.now())
    },
    {
        'id': 4,
        'reference_id': 4,
        'version': 'test_4',
        'init_date': datetime.date(datetime.now())
    },

]
REF_VERSIONS_TEST_MONGTH_AGO = [
    {
        'id': 5,
        'reference_id': 1,
        'version': 'test_old',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 6,
        'reference_id': 5,
        'version': 'test_5',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 7,
        'reference_id': 6,
        'version': 'test_6',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 8,
        'reference_id': 7,
        'version': 'test_7',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 9,
        'reference_id': 8,
        'version': 'test_8',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 10,
        'reference_id': 9,
        'version': 'test_9',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 11,
        'reference_id': 10,
        'version': 'test_10',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
    {
        'id': 12,
        'reference_id': 11,
        'version': 'test_11',
        'init_date': datetime.date(datetime.now() - timedelta(days=30))
    },
]
TEST_REFERENCE = 1
TEST_CURRENT_VERSION=1
TEST_WEEK_AGO_VERSION = 5
TEST_CURRENT_ELEMENT = {
    'code1': 'some1',
    'code2': 'some2',
    'code3': 'some3',
    'code4': 'some4',
    'code5': 'some5',
    'code6': 'some6',
    'code7': 'some7',
    'code8': 'some8',
    'code9': 'some9',
    'code10': 'some10',
    'code11': 'some11',
}
# элементы для версии 1 справочника 1
ELEMENTS_TEST_CURRENT = [
    {
        'id': 1,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code1',
        'value': TEST_CURRENT_ELEMENT['code1']
    },
    {
        'id': 2,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code2',
        'value': TEST_CURRENT_ELEMENT['code2']
    },
    {
        'id': 3,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code3',
        'value': TEST_CURRENT_ELEMENT['code3']
    },
    {
        'id': 4,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code4',
        'value': TEST_CURRENT_ELEMENT['code4']
    },
    {
        'id': 5,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code5',
        'value': TEST_CURRENT_ELEMENT['code5']
    },
    {
        'id': 6,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code6',
        'value': TEST_CURRENT_ELEMENT['code6']
    },
    {
        'id': 7,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code7',
        'value': TEST_CURRENT_ELEMENT['code7']
    },
    {
        'id': 8,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code8',
        'value': TEST_CURRENT_ELEMENT['code8']
    },
    {
        'id': 9,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code9',
        'value': TEST_CURRENT_ELEMENT['code9']
    },
    {
        'id': 10,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code10',
        'value': TEST_CURRENT_ELEMENT['code10']
    },
    {
        'id': 11,
        'ref_version_id': TEST_CURRENT_VERSION,
        'code': 'code11',
        'value': TEST_CURRENT_ELEMENT['code11']
    },
]

TEST_WEEK_AGO_ELEMENT = {
    'code10': 'somess1',
    'code20': 'somessss2',
    'code30': 'somesssss3'
}
# элементы для версии 5 справочника 1
ELEMENTS_TEST_WEEK_AGO = [
    {
        'id': 12,
        'ref_version_id': TEST_WEEK_AGO_VERSION,
        'code': 'code10',
        'value': TEST_WEEK_AGO_ELEMENT['code10']
    },
    {
        'id': 13,
        'ref_version_id': TEST_WEEK_AGO_VERSION,
        'code': 'code20',
        'value': TEST_WEEK_AGO_ELEMENT['code20']
    },
    {
        'id': 14,
        'ref_version_id': TEST_WEEK_AGO_VERSION,
        'code': 'code30',
        'value': TEST_WEEK_AGO_ELEMENT['code30']
    }
]
