import unittest

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import ACQUIRER_ID, MERCHANT_ID
from worldline.acquiring.sdk.authentication.oauth2_exception import OAuth2Exception
from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.v1.authorization_exception import AuthorizationException


class CustomOAuth2ScopesTest(unittest.TestCase):
    def test_with_valid_scopes(self):
        for oauth2_scopes in ["processing_dcc_rate", "processing_dcc_rate services_ping", "", None]:
            with self.subTest(oauth2_scopes=oauth2_scopes):
                configuration = init_utils.create_communicator_configuration()
                configuration.oauth2_scopes = oauth2_scopes

                with Factory.create_client_from_configuration(configuration) as client:
                    request = init_utils.get_dcc_rate_request()
                    response = client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).dynamic_currency_conversion().request_dcc_rate(request)
                    init_utils.assert_dcc_rate_response(self, request, response)

    def test_with_missing_scopes(self):
        configuration = init_utils.create_communicator_configuration()
        configuration.oauth2_scopes = "services_ping"

        with Factory.create_client_from_configuration(configuration) as client:
            request = init_utils.get_dcc_rate_request()

            with self.assertRaises(AuthorizationException):
                client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).dynamic_currency_conversion().request_dcc_rate(request)

    def test_with_invalid_scope(self):
        configuration = init_utils.create_communicator_configuration()
        configuration.oauth2_scopes = "processing_dcc_rate invalid_scope"

        with Factory.create_client_from_configuration(configuration) as client:
            request = init_utils.get_dcc_rate_request()

            with self.assertRaises(OAuth2Exception) as error:
                client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).dynamic_currency_conversion().request_dcc_rate(request)
            self.assertRegex(str(error.exception), "There was an error while retrieving the OAuth2 access token: invalid_scope - .*")


if __name__ == '__main__':
    unittest.main()
