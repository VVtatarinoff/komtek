from datetime import datetime, timedelta
import pytest

from references.models import RefTitles, RefVersions, Elements
from references.tests.fixtures.db_fixtures import (
    REF_TITLE_TEST, REF_VERSIONS_TEST_CURRENT,
    REF_VERSIONS_TEST_MONGTH_AGO, ELEMENTS_TEST_CURRENT,
    ELEMENTS_TEST_WEEK_AGO)


@pytest.fixture
def setup_ref_titles(db):
    refs = []
    for ref in REF_TITLE_TEST:
        refs.append(RefTitles.objects.create(**ref))
    return refs


@pytest.fixture
def setup_ref_versions(db, setup_ref_titles):
    vers = []
    for ver in (REF_VERSIONS_TEST_CURRENT + REF_VERSIONS_TEST_MONGTH_AGO):
        vers.append(RefVersions.objects.create(**ver))
    return vers


@pytest.fixture
def setup_elements(db, setup_ref_versions):
    elems = []
    for element in (ELEMENTS_TEST_CURRENT + ELEMENTS_TEST_WEEK_AGO):
        elems.append(Elements.objects.create(**element))
    return elems

@pytest.fixture
def week_ago():
    date = datetime.date(datetime.now())
    date -= timedelta(days=14)
    return date.strftime("%Y-%m-%d")

@pytest.fixture
def year_ago():
    date = datetime.date(datetime.now())
    date -= timedelta(days=365)
    return date.strftime("%Y-%m-%d")