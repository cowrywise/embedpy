import json
import requests
from embed.errors import EmbedError, EmbedConnectionError
from embed.errors import CredentialsError, ServerError
from embed.version import __version__


class HTTPClient(object):
    def __init__(self, verify_ssl_certs=True):
        self._verify_ssl_certs = verify_ssl_certs
        self.kwargs = {}
        self._content = None
        self._status_code = None

    def request(self, method, url, headers, post_data=None):
        raise NotImplementedError("HTTPClient subclasses need to implement`request`")


class APIResponse(HTTPClient):
    TIMEOUT = 40

    def __init__(self, response=None, status=None):
        self._response = response
        self._status = status
        self._headers = {
            "User-Agent": f"Cowrywise/embed-python-{__version__}",
            "Content-Type": "application/json",
        }
        super(APIResponse, self).__init__()

    def get_essential_details(self, method, url, payload=None):
        self._response, self._status = self.request(
            method, url, self._headers, post_data=payload
        )
        return self._response, self._status

    def request(self, method, url, headers, post_data=None):
        if self._verify_ssl_certs:
            self.kwargs["verify"] = True
        else:
            self.kwargs["verify"] = False

        self._content, self._status_code = None, None
        try:
            try:
                result = requests.request(
                    method,
                    url,
                    headers=headers,
                    data=post_data,
                    timeout=self.TIMEOUT,
                    **self.kwargs,
                )
            except TypeError as _exc:
                raise EmbedError(f"Error encountered: {_exc}")

            try:
                self._content = (
                    lambda content: json.loads(content) if content else None
                )(result.content)
            except json.decoder.JSONDecodeError:
                pass
            self._status_code = result.status_code
        except Exception as _exc:
            self._error_message(_exc)

        return self._content, self._status_code

    @staticmethod
    def _error_message(exc):
        if isinstance(exc, requests.exceptions.RequestException):
            err = "%s: %s" % (type(exc).__name__, str(exc))
        else:
            err = f"{type(exc).__name__} was raised"
            if str(exc):
                err += " with error message %s" % (str(exc),)
            else:
                err += " with no error message"
        raise EmbedConnectionError(f"(Network error: {err})")

    @property
    def response(self):
        return self._response

    @property
    def status(self):
        return self._status


class APISession(APIResponse):
    def __init__(self, base_url, client_id, client_secret, api_version):
        super(APISession, self).__init__()

        self._base_url = base_url
        self._api_version = api_version
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = f"{self.base_url}/o/token/"
        self._grant_type = "client_credentials"
        self._headers.update({"Content-Type": "application/x-www-form-urlencoded"})
        self._access_token, _ = self._get_access_token()

    def _get_access_token(self):
        payload = f"grant_type={self._grant_type}&client_id={self._client_id}&client_secret={self._client_secret}"
        response, status = self.request(
            "POST", self._token_url, self._headers, post_data=payload
        )
        if response is None:
            if status >= 500:
                raise ServerError(
                    f"Server error. Please contact support. Error: {status}."
                )
            else:
                raise CredentialsError(
                    f"Unable to authenticate with client credentials. Error {status}."
                )
        if status == 401:
            raise CredentialsError(
                f"Unable to authenticate with client credentials. Error {status}."
            )
        return response.get("access_token"), status

    @property
    def token(self):
        return self._access_token

    @property
    def api_version(self):
        return self._api_version

    @property
    def base_url(self):
        return self._base_url

    def __str__(self):
        return f"{self._base_url} - {self._token} - {self._api_version}"
