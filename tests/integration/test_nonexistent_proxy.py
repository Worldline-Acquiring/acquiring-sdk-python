import unittest
import configparser

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import ACQUIRER_ID, MERCHANT_ID

from worldline.acquiring.sdk.communicator_configuration import CommunicatorConfiguration
from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.proxy_configuration import ProxyConfiguration
from worldline.acquiring.sdk.communication.communication_exception import CommunicationException


class ProxyTest(unittest.TestCase):
    def test_connect_nonexistent_proxy(self):
        """Try connecting to a nonexistent proxy and assert it fails to connect to it"""
        parser = configparser.ConfigParser()
        parser.read(init_utils.PROPERTIES_URL_PROXY)
        communicator_config = CommunicatorConfiguration(parser, connect_timeout=1, socket_timeout=1,
                                                        oauth2_client_id=init_utils.OAUTH2_CLIENT_ID,
                                                        oauth2_client_secret=init_utils.OAUTH2_CLIENT_SECRET,
                                                        oauth2_token_uri=init_utils.OAUTH2_TOKEN_URI,
                                                        proxy_configuration=ProxyConfiguration(
                                                            host="localhost", port=65535,
                                                            username="arg", password="blarg")
                                                        )
        with Factory.create_client_from_configuration(communicator_config) as client:
            with self.assertRaises(CommunicationException):
                request = init_utils.get_dcc_rate_request()
                client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).dynamic_currency_conversion().request_dcc_rate(request)


if __name__ == '__main__':
    unittest.main()
