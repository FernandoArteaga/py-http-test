import pytest
from requests import Session
from requests_mock import Adapter


@pytest.fixture(scope="session")
def session():
    session = Session()
    yield session


@pytest.fixture(scope="session")
def adapter(session):
    adapter = Adapter()
    session.mount('mock://', adapter)
    yield adapter
