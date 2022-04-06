import os

import pytest
from embed.errors import CredentialsError
from embed.client import Client


def test_missing_client_id_and_secret():
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


def test_client_has_all_resources(mocker, api_session):
    mocker.patch("embed.common.APISession._get_access_token", lambda x: ("token", 200))
    client_id = "CWRY-test_client_id"
    client_secret = "CWRY-SECRET-test_client_secret"
    base_url = "http://fake.url"
    client = Client(client_id, client_secret, base_url)

    # get modules in client object
    properties = list(
        filter(lambda x: x.islower() and not x.startswith("_"), client.__dir__())
    )
    modules_in_client = set()
    for prop in properties:
        mod_name = getattr(client, prop).__class__.__module__
        if mod_name.startswith("embed.resources"):
            modules_in_client.add(mod_name)

    # get modules in embed/resources directory
    modules = os.listdir(
        os.path.join(os.path.dirname(__file__), "..", "embed", "resources")
    )
    modules = {
        f"embed.resources.{x}".strip(".py") for x in modules if not x.startswith("_")
    }

    # check that ``modules`` and ``modules_in_client`` has the same content
    # this happens if the mutual difference of both sets is an empty set
    assert not (
        modules ^ modules_in_client
    ), "Some modules in embed.resources are not mapped to embed.common.Client"


# def test_api_session(mocker):
#     def get_access_token(self):
#         return 'token', 200
#     mocker.patch('embed.common.APISession._get_access_token', get_access_token)
#     sess = APISession('https://fake.url', 'abc', 'xyz', 'v1')
#     assert sess.token == 'token'
#     assert sess.api_version == 'v1'
