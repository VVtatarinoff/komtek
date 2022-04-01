import pytest

from references.models import RefTitles, RefVersions, Elements
from references.tests.fixtures.db_fixtures import (
    REF_TITLE_TEST, REF_VERSIONS_TEST, ELEMENTS_TEST)


@pytest.fixture
def setup_ref_titles(db):
    refs = []
    for ref in REF_TITLE_TEST:
        refs.append(RefTitles.objects.create(**ref))
    return refs


@pytest.fixture
def setup_ref_versions(db, setup_ref_titles):
    vers = []
    for ver in REF_VERSIONS_TEST:
        vers.append(RefVersions.objects.create(**ver))
    return vers


@pytest.fixture
def setup_elements(db, setup_ref_versions):
    elems = []
    for element in ELEMENTS_TEST:
        elems.append(Elements.objects.create(**element))
    return elems
