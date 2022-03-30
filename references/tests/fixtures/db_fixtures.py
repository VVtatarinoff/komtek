import datetime

REF_TITLE_TEST = [
    {'id': 1,
     'name': 'first',
     'short_name': 'first',
     'description': 'first test reference db'
     },
    {'id': 2,
     'name': 'second',
     'short_name': 'second',
     'description': 'second test reference db'
     },
    {'id': 3,
     'name': 'third',
     'short_name': 'third',
     'description': 'third test reference db'
     }
]

REF_VERSIONS_TEST = [
    {
        'id': 1,
        'reference_id': 1,
        'version': 'first_1',
        'init_date': datetime.date(2022, 1, 1)
    },
    {
        'id': 2,
        'reference_id': 1,
        'version': 'first_2',
        'init_date': datetime.date(2021, 1, 1)
    },
    {
        'id': 3,
        'reference_id': 2,
        'version': 'second_1',
        'init_date': datetime.date(2022, 1, 1)
    },
    {
        'id': 4,
        'reference_id': 3,
        'version': 'third_1',
        'init_date': datetime.date(2020, 2, 1)
    },
]

ELEMENTS_TEST = [
    {
        'id': 1,
        'ref_version': 1,
        'code': 'first element first ref',
        'value': 'some first value'
    },
{
        'id': 2,
        'ref_version': 2,
        'code': 'first element first ref',
        'value': 'some first old value'
    },
{
        'id': 3,
        'ref_version': 3,
        'code': 'first element second ref',
        'value': 'some second value'
    },
{
        'id': 4,
        'ref_version': 4,
        'code': 'first element third ref',
        'value': 'some third value'
    },

]
