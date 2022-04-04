import secrets
import typing as t

import pytest
from embed.common import APISession


@pytest.fixture()
def api_session(mocker):
    def get_access_token(self):
        return "token", 200

    mocker.patch("embed.common.APISession._get_access_token", get_access_token)
    session = APISession("https://fake.url", "client_id_xyz", "client_secret_abc", "v1")
    return session


@pytest.fixture(scope="session")
def smoke_helper():
    class Smoke:
        BASE_URL_STAGING = "http://127.0.0.1:8000"
        CLIENT_ID = "CWRY-htZMzbGaEzTYJmQPISK7bHNuVmHecgSLPShRuzdU"
        CLIENT_SECRET = (
            "CWRY-SECRET-bfc7581q2klRJe8FiFGsVDmB1w32BIQXFILVMLj9iCHs"
            "zMBVJSDoOMGF7WhEeyolAxRSCsU8vBzdKbf4hsLBOVuC7sEx7Qc2eEyJ"
            "hl7wBacO9ElyqEShzGSFykNxWenp"
        )
        CLIENT_VERSION = "v1"
        api_session = APISession(
            BASE_URL_STAGING, CLIENT_ID, CLIENT_SECRET, CLIENT_VERSION
        )
        # other details
        session_hash = secrets.token_hex(4)
        account: t.Dict = {}  # session persistent dict containing account details

    return Smoke()
