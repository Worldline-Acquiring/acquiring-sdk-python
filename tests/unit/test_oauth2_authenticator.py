import os
import unittest
import uuid
import tests.file_utils as file_utils

from urllib.parse import urlparse

from tests.unit.server_mock_utils import create_server_listening
from tests.unit.test_factory import PROPERTIES_URI_OAUTH2

from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.authentication.oauth2_authenticator import OAuth2Authenticator
from worldline.acquiring.sdk.authentication.oauth2_exception import OAuth2Exception


class OAuth2AuthenticatorTest(unittest.TestCase):
    """Tests that the OAuth2Authenticator is capable of providing bearer tokens"""

    def setUp(self):
        self.configuration = Factory.create_configuration(PROPERTIES_URI_OAUTH2, str(uuid.uuid4()), str(uuid.uuid4()))
        self.configuration.connect_timeout = 1000
        self.configuration.socket_timeout = 1000

        self.call_count = 0

    def test_authentication_success(self):
        response_body = read_resource("oauth2AccessToken.json")
        handler = self.create_handler(response_code=200, body=response_body)
        with create_server_listening(handler) as address:  # start server to listen to request
            self.configuration.oauth2_token_uri = address + "/auth/realms/api/protocol/openid-connect/token"

            authenticator = OAuth2Authenticator(self.configuration)

            for _ in range(0, 3):
                authorization = authenticator.get_authorization(None, urlparse("http://domain/local/anything/operations"), None)

                self.assertEqual("Bearer accessToken", authorization)

            self.assertEqual(1, self.call_count)

    def test_authentication_invalid_client(self):
        response_body = read_resource("oauth2AccessToken.invalidClient.json")
        handler = self.create_handler(response_code=401, body=response_body)
        with create_server_listening(handler) as address:  # start server to listen to request
            self.configuration.oauth2_token_uri = address + "/auth/realms/api/protocol/openid-connect/token"

            authenticator = OAuth2Authenticator(self.configuration)

            for _ in range(0, 3):
                with self.assertRaises(OAuth2Exception) as cm:
                    authenticator.get_authorization(None, urlparse("http://domain/local/anything/operations"), None)

                oauth2_exception = cm.exception
                self.assertEqual(
                    "There was an error while retrieving the OAuth2 access token: unauthorized_client - INVALID_CREDENTIALS: Invalid client credentials",
                    str(oauth2_exception))

            self.assertEqual(3, self.call_count)

    def test_authentication_expired_token(self):
        response_body = read_resource("oauth2AccessToken.expired.json")
        handler = self.create_handler(response_code=200, body=response_body)
        with create_server_listening(handler) as address:  # start server to listen to request
            self.configuration.oauth2_token_uri = address + "/auth/realms/api/protocol/openid-connect/token"

            authenticator = OAuth2Authenticator(self.configuration)

            for _ in range(0, 3):
                authorization = authenticator.get_authorization(None, urlparse("http://domain/local/anything/operations"), None)

                self.assertEqual("Bearer expiredAccessToken", authorization)

            self.assertEqual(3, self.call_count)

    def create_handler(self, response_code=200, body='{}'):
        """
        Creates a request handler that receives the request on the server side

        :param response_code: status code of the desired response
        :param body: the body of the response message to return, it should be in json format
        """
        def handler_func(handler):
            handler.protocol_version = 'HTTP/1.1'
            handler.send_response(response_code)
            handler.send_header('Content-Type', 'application/json')
            handler.end_headers()
            handler.wfile.write(bytes(body, "utf-8"))
            self.call_count = self.call_count + 1
        return handler_func


def read_resource(relative_path):
    return file_utils.read_file(os.path.join("authentication", relative_path))
