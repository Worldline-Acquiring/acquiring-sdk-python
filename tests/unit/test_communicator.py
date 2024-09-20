# -*-coding: UTF-8 -*-
import unittest

from urllib.parse import urlparse
from unittest.mock import MagicMock

from worldline.acquiring.sdk.communicator import Communicator
from worldline.acquiring.sdk.authentication.authenticator import Authenticator
from worldline.acquiring.sdk.communication.connection import Connection
from worldline.acquiring.sdk.communication.metadata_provider import MetadataProvider
from worldline.acquiring.sdk.communication.request_param import RequestParam
from worldline.acquiring.sdk.json.default_marshaller import DefaultMarshaller


class CommunicatorTest(unittest.TestCase):
    """Contains tests that test if the communicator can construct proper urls
    if given the base url, a relative url and possibly a list of request parameters
    """

    def test_to_uri_without_request_parameters(self):
        """Tests if the communicator can correctly construct an url using a known base url and a relative url"""
        communicator = Communicator(api_endpoint=urlparse("https://api.preprod.acquiring.worldline-solutions.com"),
                                    connection=MagicMock(spec=Connection, autospec=True),
                                    authenticator=MagicMock(spec=Authenticator, autospec=True),
                                    metadata_provider=MetadataProvider("Worldline"),
                                    marshaller=DefaultMarshaller.instance())

        uri1 = communicator._to_absolute_uri("services/v1/100812/520000214/dcc-rates", [])
        uri2 = communicator._to_absolute_uri("/services/v1/100812/520000214/dcc-rates", [])

        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com/services/v1/100812/520000214/dcc-rates", uri1.geturl())
        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com/services/v1/100812/520000214/dcc-rates", uri2.geturl())

    def test_to_uri_with_request_parameters(self):
        """Tests if the communicator can correctly construct an url
        using a known base url, a relative url and a list of request parameters
        """
        requestparams = [RequestParam("amount", "123"), RequestParam("source", "USD"),
                         RequestParam("target", "EUR"), RequestParam("dummy", "é&%=")]
        communicator = Communicator(api_endpoint=urlparse("https://api.preprod.acquiring.worldline-solutions.com"),
                                    connection=MagicMock(spec=Connection, autospec=True),
                                    authenticator=MagicMock(spec=Authenticator, autospec=True),
                                    metadata_provider=MetadataProvider("Worldline"),
                                    marshaller=DefaultMarshaller.instance())

        uri1 = communicator._to_absolute_uri("services/v1/100812/520000214/dcc-rates", requestparams)
        uri2 = communicator._to_absolute_uri("/services/v1/100812/520000214/dcc-rates", requestparams)

        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com/services/v1/100812/520000214/dcc-rates"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", uri1.geturl())
        self.assertEqual("https://api.preprod.acquiring.worldline-solutions.com/services/v1/100812/520000214/dcc-rates"
                         "?amount=123&source=USD&target=EUR&dummy=%C3%A9%26%25%3D", uri2.geturl())


if __name__ == '__main__':
    unittest.main()
