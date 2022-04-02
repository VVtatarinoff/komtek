import json
import pytest
from rest_framework.reverse import reverse_lazy, reverse
from references.tests.fixtures.db_fixtures import (
    ELEMENTS_TEST_CURRENT, ELEMENTS_TEST_WEEK_AGO,
    REF_VERSIONS_TEST_MONGTH_AGO, TEST_CURRENT_ELEMENT,
    TEST_WEEK_AGO_ELEMENT, TEST_WEEK_AGO_VERSION, TEST_REFERENCE)

PAGE = 'validation'


@pytest.mark.django_db
def test_validate_current_version(setup_elements, client):
    response = client.post(
        reverse_lazy(PAGE, kwargs={'pk': TEST_REFERENCE}),
        content_type='application/json',
        data=TEST_CURRENT_ELEMENT)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is True


@pytest.mark.django_db
def test_validate_old_version(setup_elements, client):
    url = f"{reverse(PAGE, kwargs={'pk': TEST_REFERENCE})}?version={TEST_WEEK_AGO_VERSION}"
    response = client.post(url,
                           content_type='application/json',
                           data=TEST_WEEK_AGO_ELEMENT)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is True
