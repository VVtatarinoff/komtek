import pytest
from rest_framework.reverse import reverse_lazy

from references.tests.fixtures.db_fixtures import REF_TITLE_TEST

PAGE = 'refs'


@pytest.mark.django_db
def test_get_current_versions(setup_ref_versions, client):
    expected_len = len(REF_TITLE_TEST)
    response = client.get(reverse_lazy(PAGE))
    assert response.status_code == 200
    assert response.data['count'] == expected_len
    assert response.accepted_media_type == 'application/json'
    assert len(response.data['results']) == 10
    n = 1
