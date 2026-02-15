import json
from embed.resources.integrations import Integration
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_cscs_onboarding(mock_get_essential_details, api_session):
    integration = Integration(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "cscs_number": "fake-cscs-number",
    }
    integration.cscs_onboarding(**test_data)
    integration.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/integration/cscs/onboarding",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_cscs_profile(mock_get_essential_details, api_session):
    integration = Integration(api_session)
    mock_get_essential_details.return_value = MagicMock()
    integration.get_cscs_profile("fake-account-id")
    integration.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/integration/cscs/onboarding?account_id=fake-account-id",
    )
