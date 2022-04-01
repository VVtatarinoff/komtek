import pytest
from rest_framework.reverse import reverse_lazy

from references.tests.fixtures.db_fixtures import (
    REF_TITLE_TEST, REF_VERSIONS_TEST_MONGTH_AGO)

PAGE = 'refs'


@pytest.mark.django_db
def test_get_current_versions(setup_ref_versions, client):
    expected_len = len(REF_TITLE_TEST)
    response = client.get(reverse_lazy(PAGE))
    assert response.status_code == 200
    assert response.data['count'] == expected_len
    assert response.accepted_media_type == 'application/json'
    assert len(response.data['results']) == min(10, expected_len)


@pytest.mark.django_db
def test_get_week_ago_versions(setup_ref_versions, client, week_ago):
    expected_len = len(REF_VERSIONS_TEST_MONGTH_AGO)
    response = client.get(reverse_lazy(PAGE), {'date': week_ago})
    assert response.status_code == 200
    assert response.data['count'] == expected_len
    assert response.accepted_media_type == 'application/json'


@pytest.mark.django_db
def test_get_year_ago_versions(setup_ref_versions, client, year_ago):
    response = client.get(reverse_lazy(PAGE), {'date': year_ago})
    assert response.status_code == 200
    assert response.data['count'] == 0
    assert response.accepted_media_type == 'application/json'


def test_content_keys(setup_ref_versions, client):
    response = client.get(reverse_lazy(PAGE))
    results = response.data['results'][0]
    assert 'id' in results
    assert 'name' in results
    assert 'short_name' in results
    assert 'description' in results
    assert 'version_name' in results
    assert 'version_id' in results
    assert 'valid_date' in results
