import pytest
from rest_framework.reverse import reverse_lazy


PAGE = 'elements'

@pytest.mark.django_db
def test_get_current_versions(setup_elements, client):
    pass