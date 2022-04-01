import pytest
from rest_framework.reverse import reverse_lazy

from references.tests.fixtures.db_fixtures import (
    ELEMENTS_TEST_CURRENT, ELEMENTS_TEST_WEEK_AGO, REF_VERSIONS_TEST_MONGTH_AGO)

PAGE = 'elements'

@pytest.mark.django_db
def test_get_current_versions(setup_elements, client):
    expected_len = len(ELEMENTS_TEST_CURRENT)
    response = client.get(reverse_lazy(PAGE, kwargs={'pk': 1}))
    assert response.status_code == 200
    assert response.data['count'] == expected_len
    assert response.accepted_media_type == 'application/json'
    assert len(response.data['results']) == min(10, expected_len)

@pytest.mark.django_db
def test_get_week_ago_versions(setup_elements, client, week_ago):
    expected_len = len(ELEMENTS_TEST_WEEK_AGO)
    response = client.get(reverse_lazy(PAGE, kwargs={'pk': 1}),
                          {'version': REF_VERSIONS_TEST_MONGTH_AGO[0]['id']})
    assert response.status_code == 200
    assert response.data['count'] == expected_len
    assert response.accepted_media_type == 'application/json'
    assert len(response.data['results']) == min(10, expected_len)