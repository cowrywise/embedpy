import pytest
from embed.common import APISession


@pytest.fixture()
def client_token():
    pass


@pytest.fixture()
def api_session(mocker):
    def get_access_token(self):
        return "token", 200

    mocker.patch("embed.common.APISession._get_access_token", get_access_token)
    session = APISession("https://fake.url", "client_id_xyz", "client_secret_abc", "v1")
    return session
