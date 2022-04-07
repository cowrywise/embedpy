from unittest.mock import patch, MagicMock

import pytest
from embed import common
from embed.errors import ValidationError


@pytest.mark.parametrize(
    ["required", "raises"],
    [
        (["arg_0", "arg_1"], False),
        (["arg_0", "arg_1", "arg_2"], False),
        (["arg_0", "arg_1", "arg_2", "arg_3"], True),
    ],
)
def test_APIResponse__validate_kwargs(required, raises):
    kwargs = {"arg_0": "val_0", "arg_1": "val_1", "arg_2": "val_2"}
    if raises:
        with pytest.raises(ValidationError):
            common.APIResponse._validate_kwargs(required, kwargs)
    else:
        common.APIResponse._validate_kwargs(required, kwargs)


@pytest.mark.parametrize(
    ["date", "raises"],
    [
        ("2020-01-18", False),
        ("2020-18-01", True),
        ("18-01-2020", True),
        ("12323242531445", True),
    ],
)
def test_APIResponse__validate_date_string(date, raises):
    if raises:
        with pytest.raises(ValidationError):
            common.APIResponse._validate_date_string(date)
    else:
        common.APIResponse._validate_date_string(date)


def test_APIResponse__format_query():
    kwargs = {"arg_0": "val_0", "arg_1": 1, "arg_2": True}

    # TODO rewrite parameter handling, use requests.request's ``params=t.Dict``
    query_path = common.APIResponse._format_query(kwargs)
    assert query_path == "arg_0=val_0&arg_1=1&arg_2=True"


@pytest.mark.parametrize(
    ("content", "expected_resp_content"),
    (('{"valid": "JSON"}', {"valid": "JSON"}), ("{invalid_json}", None)),
)
@patch("requests.request")
def test_APIResponse_request(mock_request, content, expected_resp_content):
    mock_request.return_value = MagicMock(content=content, status_code=200)
    response_obj = common.APIResponse(response="test_response", status="test_status")
    resp = response_obj.request("GET", "https://fake.url", headers={})
    assert resp == (expected_resp_content, 200)

    assert response_obj.response == "test_response"
    assert response_obj.status == "test_status"
