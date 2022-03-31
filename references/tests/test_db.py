from copy import copy

import pytest

from references.models import RefVersions
from references.tests.fixtures.db_fixtures import REF_VERSIONS_TEST


@pytest.mark.django_db
def test_create_dublicate_name_version(setup_ref_versions):
    new_ver = copy(REF_VERSIONS_TEST[0])
    new_ver.pop('id')
    init_len = len(RefVersions.objects.all())
    with pytest.raises(Exception) as e:
        RefVersions.objects.create(**new_ver)
    assert e.match('повторяющееся значение ключа нарушает ограничение уникальности')


@pytest.mark.django_db
def test_create_dublicate_date_version(setup_ref_versions):
    new_ver = copy(REF_VERSIONS_TEST[0])
    new_ver.pop('id')
    new_ver['version'] += ' test date'
    init_len = len(RefVersions.objects.all())
    with pytest.raises(Exception) as e:
        RefVersions.objects.create(**new_ver)
    assert e.match('повторяющееся значение ключа нарушает ограничение уникальности')


@pytest.mark.django_db
def test_create_null_version(setup_ref_versions):
    new_ver = copy(REF_VERSIONS_TEST[0])
    new_ver.pop('id')
    new_ver['version'] = ''
    init_len = len(RefVersions.objects.all())
    with pytest.raises(Exception) as e:
        RefVersions.objects.create(**new_ver)
    assert e.match('повторяющееся значение ключа нарушает ограничение уникальности')
