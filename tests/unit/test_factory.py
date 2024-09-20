import os
import unittest
import warnings

from urllib.parse import urlparse

from tests.unit.test_default_connection import DefaultConnectionTest

from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.authentication.authorization_type import AuthorizationType
from worldline.acquiring.sdk.authentication.oauth2_authenticator import OAuth2Authenticator
from worldline.acquiring.sdk.communication.default_connection import DefaultConnection
from worldline.acquiring.sdk.communication.metadata_provider import MetadataProvider
from worldline.acquiring.sdk.json.default_marshaller import DefaultMarshaller

PROPERTIES_URI_OAUTH2 = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.oauth2.ini"))
OAUTH2_CLIENT_ID = "someId"
OAUTH2_CLIENT_SECRET = "someSecret"


class FactoryTest(unittest.TestCase):
    """Tests that the factory is capable of correctly creating communicators and communicator configurations"""

    def test_create_configuration(self):
        """Tests that the factory is correctly able to create a communicator configuration"""
        configuration = Factory.create_configuration(PROPERTIES_URI_OAUTH2, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)
        self.assertEqual(urlparse("https://api.preprod.acquiring.worldline-solutions.com"), configuration.api_endpoint)
        self.assertEqual(AuthorizationType.get_authorization("OAuth2"), configuration.authorization_type)
        self.assertEqual(1000, configuration.connect_timeout)
        self.assertEqual(1000, configuration.socket_timeout)
        self.assertEqual(100, configuration.max_connections)
        self.assertEqual(OAUTH2_CLIENT_ID, configuration.oauth2_client_id)
        self.assertEqual(OAUTH2_CLIENT_SECRET, configuration.oauth2_client_secret)
        self.assertIsNone(configuration.proxy_configuration)

    # noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
    def test_create_communicator(self):
        """Tests that the factory is correctly able to create a communicator"""
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI_OAUTH2, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)

        self.assertIs(communicator.marshaller, DefaultMarshaller.instance())

        connection = communicator._Communicator__connection
        self.assertIsInstance(connection, DefaultConnection)
        DefaultConnectionTest.assertConnection(self, connection, 1000, 1000, 100, None)

        authenticator = communicator._Communicator__authenticator
        self.assertIsInstance(authenticator, OAuth2Authenticator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(OAUTH2_CLIENT_ID, authenticator._OAuth2Authenticator__client_id)
            self.assertEqual(OAUTH2_CLIENT_SECRET, authenticator._OAuth2Authenticator__client_secret)

        metadata_provider = communicator._Communicator__metadata_provider
        self.assertIsInstance(metadata_provider, MetadataProvider)
        request_headers = metadata_provider.metadata_headers
        self.assertEqual(1, len(request_headers))
        self.assertEqual("X-WL-ServerMetaInfo", request_headers[0].name)

    # noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
    def test_create_communicator_with_authorization_type_oauth2(self):
        """Tests that the factory is correctly able to create a communicator"""
        communicator = Factory.create_communicator_from_file(PROPERTIES_URI_OAUTH2, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET)

        authenticator = communicator._Communicator__authenticator
        self.assertIsInstance(authenticator, OAuth2Authenticator)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.assertEqual(OAUTH2_CLIENT_ID, authenticator._OAuth2Authenticator__client_id)
            self.assertEqual(OAUTH2_CLIENT_SECRET, authenticator._OAuth2Authenticator__client_secret)


if __name__ == '__main__':
    unittest.main()
