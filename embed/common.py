import json
import requests
from embed.errors import APIError, APIConnectionError


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
        self._headers = {}
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
                print(result.request.headers)
                print(result.request.url)
            except TypeError as _exc:
                raise APIError(f"Error encountered: {_exc}")

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
        raise APIConnectionError(f"(Network error: {err})")

    @property
    def response(self):
        return self._response

    @property
    def status(self):
        return self._status
