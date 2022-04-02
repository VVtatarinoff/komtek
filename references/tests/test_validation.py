import pytest
from rest_framework.reverse import reverse_lazy, reverse
from references.tests.fixtures.db_fixtures import (
    TEST_CURRENT_ELEMENT,
    TEST_WEEK_AGO_ELEMENT, TEST_WEEK_AGO_VERSION, TEST_REFERENCE)

PAGE = 'validation'


@pytest.mark.django_db
def test_validate_current_version(setup_elements, client):
    """тестирование текущей версии справочника с валидными данными"""
    response = client.post(
        reverse_lazy(PAGE, kwargs={'pk': TEST_REFERENCE}),
        content_type='application/json',
        data=TEST_CURRENT_ELEMENT)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is True


@pytest.mark.django_db
def test_validate_old_version(setup_elements, client):
    """тестирование прошлой версии справочника с валидными данными"""
    url = f"{reverse(PAGE, kwargs={'pk': TEST_REFERENCE})}" \
          f"?version={TEST_WEEK_AGO_VERSION}"
    response = client.post(url,
                           content_type='application/json',
                           data=TEST_WEEK_AGO_ELEMENT)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is True


@pytest.mark.django_db
def test_wrong_value_current_version(setup_elements, client):
    """тестирование текущей версии справочника с некорректными данными"""
    wrong_values = dict()
    wrong_values.update(TEST_CURRENT_ELEMENT)
    wrong_values['code1'] += 'wrong'
    response = client.post(
        reverse_lazy(PAGE, kwargs={'pk': TEST_REFERENCE}),
        content_type='application/json',
        data=wrong_values)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is False


@pytest.mark.django_db
def test_wrong_key_current_version(setup_elements, client):
    """тестирование текущей версии справочника с некорректным ключом"""
    wrong_values = dict()
    wrong_values.update(TEST_CURRENT_ELEMENT)
    wrong_values['test'] = 'wrong'
    response = client.post(
        reverse_lazy(PAGE, kwargs={'pk': TEST_REFERENCE}),
        content_type='application/json',
        data=wrong_values)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is False


@pytest.mark.django_db
def test_no_data_current_version(setup_elements, client):
    """тестирование текущей версии справочника с некорректным ключом"""
    wrong_values = dict()
    response = client.post(
        reverse_lazy(PAGE, kwargs={'pk': TEST_REFERENCE}),
        content_type='application/json',
        data=wrong_values)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data['result'] is False
