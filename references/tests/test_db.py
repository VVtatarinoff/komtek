import pytest

from references.models import RefVersions
from references.tests.fixtures.db_fixtures import REF_VERSIONS_TEST


@pytest.mark.django_db
def test_create_dublicate_version(setup_ref_versions):
    new_ver = REF_VERSIONS_TEST[0]
    new_ver['id'] = 1000
    init_len = len(RefVersions.objects.all())
    with pytest.raises(Exception) as e:
        RefVersions.objects.create(**new_ver)
    assert e.match('Не может быть одинаковых версий для одного справочника')
    assert init_len == len(RefVersions.objects.all())

