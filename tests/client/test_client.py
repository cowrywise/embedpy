import pytest
from embed.errors import CredentialsError
from embed.client import Client
from embed.common import APISession


def test_missing_client_id_secret():
    with pytest.raises(CredentialsError) as exc:
        Client()
    assert "Provide client id or set CLIENT_ID as environment variable." == str(
        exc.value
    )


def test_missing_client_id():
    with pytest.raises(CredentialsError) as exc:
        Client(client_secret="xxx")
    assert "Provide client id or set CLIENT_ID as environment variable." == str(
        exc.value
    )


def test_missing_client_secret():
    with pytest.raises(CredentialsError) as exc:
        Client(client_id="xxx")
    assert "Provide client secret or set CLIENT_SECRET in environment variable." == str(
        exc.value
    )


# def test_api_session(mocker):
#     def get_access_token(self):
#         return 'token', 200
#     mocker.patch('embed.common.APISession._get_access_token', get_access_token)
#     sess = APISession('https://fake.url', 'abc', 'xyz', 'v1')
#     assert sess.token == 'token'
#     assert sess.api_version == 'v1'
