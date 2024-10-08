import configparser
import unittest

from worldline.acquiring.sdk.authentication.authorization_type import AuthorizationType
from worldline.acquiring.sdk.communicator_configuration import CommunicatorConfiguration


class CommunicatorConfigurationTest(unittest.TestCase):
    """Contains tests testing that the correct communicator configuration can be made from a properties file"""

    def setUp(self):
        """Initialize a set of commonly used configurations"""
        self.config = configparser.ConfigParser()

        self.config.add_section("AcquiringSDK")
        self.config.set('AcquiringSDK', 'acquiring.api.endpoint.host', "api.preprod.acquiring.worldline-solutions.com")
        self.config.set('AcquiringSDK', 'acquiring.api.authorizationType', 'OAuth2')
        self.config.set('AcquiringSDK', 'acquiring.api.oauth2.tokenUri', 'https://sso.preprod.acquiring.worldline-solutions.com/auth/realms/acquiring_api/protocol/openid-acquiring/token')
        self.config.set('AcquiringSDK', 'acquiring.api.connectTimeout', '20')
        self.config.set('AcquiringSDK', 'acquiring.api.socketTimeout', '10')

    def tearDown(self):
        self.config = None

    def assertDefaults(self, communicator_config):
        """Tests commonly used settings for testing url, authorization type, timeouts and max_connections"""
        #                                                           this argument should not be needed    VV
        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.get_authorization("OAuth2"), communicator_config.authorization_type)
        self.assertEqual(20, communicator_config.connect_timeout)
        self.assertEqual(10, communicator_config.socket_timeout)

        self.assertEqual(CommunicatorConfiguration().DEFAULT_MAX_CONNECTIONS, communicator_config.max_connections)

    def test_construct_from_properties_without_proxy(self):
        """Test if a CommunicatorConfiguration can be constructed correctly from a list of properties"""

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.authorization_id)
        self.assertIsNone(communicator_config.authorization_secret)
        self.assertIsNone(communicator_config.proxy_configuration)
        self.assertIsNone(communicator_config.integrator)
        self.assertIsNone(communicator_config.shopping_cart_extension)

    def test_construct_from_properties_with_proxy_without_authentication(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly from settings including a proxy"""
        self.config.set('AcquiringSDK', "acquiring.api.proxy.uri", "http://proxy.example.org:3128")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.authorization_id)
        self.assertIsNone(communicator_config.authorization_secret)
        proxy_config = communicator_config.proxy_configuration
        self.assertIsNotNone(proxy_config)
        self.assertEqual("http", proxy_config.scheme)
        self.assertEqual("proxy.example.org", proxy_config.host)
        self.assertEqual(3128, proxy_config.port)
        self.assertIsNone(proxy_config.username)
        self.assertIsNone(proxy_config.password)

    def test_construct_from_properties_with_proxy_authentication(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly
        from settings with a proxy and authentication
        """
        self.config.set('AcquiringSDK', "acquiring.api.proxy.uri", "http://proxy.example.org:3128")
        self.config.set('AcquiringSDK', "acquiring.api.proxy.username", "proxy-username")
        self.config.set('AcquiringSDK', "acquiring.api.proxy.password", "proxy-password")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.authorization_id)
        self.assertIsNone(communicator_config.authorization_secret)
        proxy_config = communicator_config.proxy_configuration
        self.assertIsNotNone(proxy_config)
        self.assertEqual("http", proxy_config.scheme)
        self.assertEqual("proxy.example.org", proxy_config.host)
        self.assertEqual(3128, proxy_config.port)
        self.assertEqual("proxy-username", proxy_config.username)
        self.assertEqual("proxy-password", proxy_config.password)

    def test_construct_from_properties_with_max_connection(self):
        """Tests if a CommunicatorConfiguration can be constructed correctly
         from settings that contain a different number of maximum connections
         """
        self.config.set("AcquiringSDK", "acquiring.api.maxConnections", "100")

        communicator_config = CommunicatorConfiguration(self.config)
        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com", communicator_config.api_endpoint.geturl())
        self.assertEqual(AuthorizationType.get_authorization("OAuth2"), communicator_config.authorization_type)
        self.assertEqual(20, communicator_config.connect_timeout)
        self.assertEqual(10, communicator_config.socket_timeout)
        self.assertEqual(100, communicator_config.max_connections)
        self.assertIsNone(communicator_config.authorization_id)
        self.assertIsNone(communicator_config.authorization_secret)
        self.assertIsNone(communicator_config.proxy_configuration)

    def test_construct_from_properties_with_host_and_scheme(self):
        """Tests that constructing a communicator configuration from a host and port correctly processes this info"""
        self.config.set("AcquiringSDK", "acquiring.api.endpoint.scheme", "http")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://api.preprod.acquiring.worldline-solutions.com", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_host_and_port(self):
        """Tests that constructing a communicator configuration from a host and port correctly processes this info"""

        self.config.set("AcquiringSDK", "acquiring.api.endpoint.port", "8443")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com:8443", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_host_scheme_port(self):
        """Tests that constructing a communicator configuration from host, scheme and port correctly processes this info
        """
        self.config.set("AcquiringSDK", "acquiring.api.endpoint.scheme", "http")
        self.config.set("AcquiringSDK", "acquiring.api.endpoint.port", "8080")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertEqual("http://api.preprod.acquiring.worldline-solutions.com:8080", communicator_config.api_endpoint.geturl())

    def test_construct_from_properties_with_metadata(self):
        """Tests that constructing a communicator configuration
        using integrator and shopping cart data constructs properly
        """
        self.config.set("AcquiringSDK", "acquiring.api.integrator", "Worldline.Integrator")
        self.config.set("AcquiringSDK", "acquiring.api.shoppingCartExtension.creator", "Worldline.Creator")
        self.config.set("AcquiringSDK", "acquiring.api.shoppingCartExtension.name", "Worldline.ShoppingCarts")
        self.config.set("AcquiringSDK", "acquiring.api.shoppingCartExtension.version", "1.0")
        self.config.set("AcquiringSDK", "acquiring.api.shoppingCartExtension.extensionId", "ExtensionId")

        communicator_config = CommunicatorConfiguration(self.config)

        self.assertDefaults(communicator_config)
        self.assertIsNone(communicator_config.authorization_id)
        self.assertIsNone(communicator_config.authorization_secret)
        self.assertIsNone(communicator_config.proxy_configuration)
        self.assertEqual("Worldline.Integrator", communicator_config.integrator)
        self.assertIsNotNone(communicator_config.shopping_cart_extension)
        self.assertEqual("Worldline.Creator", communicator_config.shopping_cart_extension.creator)
        self.assertEqual("Worldline.ShoppingCarts", communicator_config.shopping_cart_extension.name)
        self.assertEqual("1.0", communicator_config.shopping_cart_extension.version)
        self.assertEqual("ExtensionId", communicator_config.shopping_cart_extension.extension_id)


if __name__ == '__main__':
    unittest.main()
