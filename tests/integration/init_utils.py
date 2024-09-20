import os
from configparser import ConfigParser
from datetime import datetime
from uuid import uuid4

from worldline.acquiring.sdk.authentication.oauth2_authenticator import OAuth2Authenticator
from worldline.acquiring.sdk.communication.default_connection import DefaultConnection
from worldline.acquiring.sdk.communication.metadata_provider import MetadataProvider
from worldline.acquiring.sdk.communicator import Communicator
from worldline.acquiring.sdk.communicator_configuration import CommunicatorConfiguration
from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.json.default_marshaller import DefaultMarshaller
from worldline.acquiring.sdk.v1.domain.amount_data import AmountData
from worldline.acquiring.sdk.v1.domain.api_payment_request import ApiPaymentRequest
from worldline.acquiring.sdk.v1.domain.api_payment_resource import ApiPaymentResource
from worldline.acquiring.sdk.v1.domain.api_payment_response import ApiPaymentResponse
from worldline.acquiring.sdk.v1.domain.card_data_for_dcc import CardDataForDcc
from worldline.acquiring.sdk.v1.domain.card_payment_data import CardPaymentData
from worldline.acquiring.sdk.v1.domain.e_commerce_data import ECommerceData
from worldline.acquiring.sdk.v1.domain.get_dcc_rate_request import GetDCCRateRequest
from worldline.acquiring.sdk.v1.domain.get_dcc_rate_response import GetDccRateResponse
from worldline.acquiring.sdk.v1.domain.payment_references import PaymentReferences
from worldline.acquiring.sdk.v1.domain.plain_card_data import PlainCardData
from worldline.acquiring.sdk.v1.domain.point_of_sale_data_for_dcc import PointOfSaleDataForDcc
from worldline.acquiring.sdk.v1.domain.transaction_data_for_dcc import TransactionDataForDcc

"""File containing a number of creation methods for integration tests"""

PROPERTIES_URL_OAUTH2 = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.oauth2.ini"))
PROPERTIES_URL_PROXY = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.proxy.ini"))
# OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET, OAUTH2_TOKEN_URI, MERCHANT_ID and ACQUIRER_ID are stored in OS and should be retrieved
OAUTH2_CLIENT_ID = os.getenv("acquiring.api.oauth2.clientId")
OAUTH2_CLIENT_SECRET = os.getenv("acquiring.api.oauth2.clientSecret")
OAUTH2_TOKEN_URI = os.getenv("acquiring.api.oauth2.tokenUri")
MERCHANT_ID = str(os.getenv("acquiring.api.merchantId"))
ACQUIRER_ID = str(os.getenv("acquiring.api.acquirerId"))
if OAUTH2_CLIENT_ID is None:
    raise EnvironmentError("could not access environment variable acquiring.api.oauth2.clientId required for testing")
if OAUTH2_CLIENT_SECRET is None:
    raise EnvironmentError("could not access environment variable acquiring.api.oauth2.clientSecret required for testing")
if OAUTH2_TOKEN_URI is None:
    raise EnvironmentError("could not access environment variable acquiring.api.oauth2.tokenUri required for testing")
if MERCHANT_ID == 'None':
    raise EnvironmentError("could not access environment variable acquiring.api.merchantId required for testing")
if ACQUIRER_ID == 'None':
    raise EnvironmentError("could not access environment variable acquiring.api.acquirerId required for testing")


def create_communicator_configuration(properties_url=PROPERTIES_URL_OAUTH2, max_connections=None):
    """Convenience method to create a communicator configuration that connects to a host stored in system variables"""
    try:
        parser = ConfigParser()
        parser.read(properties_url)
        with open(properties_url) as f:
            parser.read_file(f)
        configuration = CommunicatorConfiguration(parser,
                                                  oauth2_client_id=OAUTH2_CLIENT_ID,
                                                  oauth2_client_secret=OAUTH2_CLIENT_SECRET,
                                                  oauth2_token_uri=OAUTH2_TOKEN_URI,
                                                  max_connections=max_connections)
    except IOError as e:
        raise RuntimeError("Unable to read configuration", e)
    host = os.getenv("acquiring.api.endpoint.host")
    if host is not None:
        scheme = os.getenv("acquiring.api.endpoint.scheme", "https")
        port = int(os.getenv("acquiring.api.endpoint.port", -1))
        configuration.api_endpoint = "{2}://{0}:{1}".format(host, port, scheme)
    return configuration


def create_communicator():
    configuration = create_communicator_configuration()
    authenticator = OAuth2Authenticator(configuration)
    return Communicator(api_endpoint=configuration.api_endpoint, authenticator=authenticator,
                        connection=DefaultConnection(3, 3), metadata_provider=MetadataProvider("Worldline"),
                        marshaller=DefaultMarshaller.instance())


def create_client(max_connections=None):
    configuration = create_communicator_configuration(max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration)


def create_client_with_proxy(max_connections=None):
    configuration = create_communicator_configuration(PROPERTIES_URL_PROXY, max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration)


def get_api_payment_request():
    request = ApiPaymentRequest()

    request.amount = AmountData()
    request.amount.amount = 200
    request.amount.currency_code = "GBP"
    request.amount.number_of_decimals = 2
    request.authorization_type = "PRE_AUTHORIZATION"
    request.transaction_timestamp = datetime.now()
    request.card_payment_data = CardPaymentData()
    request.card_payment_data.card_entry_mode = "ECOMMERCE"
    request.card_payment_data.allow_partial_approval = False
    request.card_payment_data.brand = "VISA"
    request.card_payment_data.capture_immediately = False
    request.card_payment_data.cardholder_verification_method = "CARD_SECURITY_CODE"
    request.card_payment_data.card_data = PlainCardData()
    request.card_payment_data.card_data.expiry_date = "122031"
    request.card_payment_data.card_data.card_number = "4176669999000104"
    request.card_payment_data.card_data.card_security_code = "012"
    request.references = PaymentReferences()
    request.references.merchant_reference = "your-order-" + str(uuid4())
    request.operation_id = str(uuid4())
    return request


def assert_payment_response(self, request: ApiPaymentRequest, response: ApiPaymentResponse):
    self.assertEqual(request.operation_id, response.operation_id)
    self.assertEqual("0", response.response_code)
    self.assertEqual("APPROVED", response.response_code_category)
    self.assertIsNotNone(response.response_code_description)
    self.assertEqual("AUTHORIZED", response.status)
    self.assertIsNotNone(response.initial_authorization_code)
    self.assertIsNotNone(response.payment_id)
    self.assertIsNotNone(response.total_authorized_amount)
    self.assertEqual(200, response.total_authorized_amount.amount)
    self.assertEqual("GBP", response.total_authorized_amount.currency_code)
    self.assertEqual(2, response.total_authorized_amount.number_of_decimals)


def assert_payment_status_response(self, payment_id: str, response: ApiPaymentResource):
    self.assertIsNotNone(response.initial_authorization_code)
    self.assertEqual(payment_id, response.payment_id)
    self.assertEqual("AUTHORIZED", response.status)


def get_dcc_rate_request(amount: int = 200):
    amount_data = AmountData()
    amount_data.amount = amount
    amount_data.currency_code = "GBP"
    amount_data.number_of_decimals = 2

    transaction_data_for_dcc = TransactionDataForDcc()
    transaction_data_for_dcc.amount = amount_data
    transaction_data_for_dcc.transaction_type = "PAYMENT"
    transaction_data_for_dcc.transaction_timestamp = datetime.now()

    point_of_sale_data_for_dcc = PointOfSaleDataForDcc()
    point_of_sale_data_for_dcc.terminal_id = "12345678"

    card_data_for_dcc = CardDataForDcc()
    card_data_for_dcc.bin = "41766699"
    card_data_for_dcc.brand = "VISA"

    request = GetDCCRateRequest()
    request.operation_id = str(uuid4())
    request.target_currency = "EUR"
    request.card_payment_data = card_data_for_dcc
    request.point_of_sale_data = point_of_sale_data_for_dcc
    request.transaction = transaction_data_for_dcc

    return request


def assert_dcc_rate_response(self, request: GetDCCRateRequest, response: GetDccRateResponse):
    self.assertIsNotNone(response.proposal)
    self.assertIsNotNone(response.proposal.original_amount)
    assert_equal_amounts(self, request.transaction.amount, response.proposal.original_amount)
    self.assertEqual(request.target_currency, response.proposal.resulting_amount.currency_code)


def assert_equal_amounts(self, expected: AmountData, actual: AmountData):
    self.assertEqual(expected.amount, actual.amount)
    self.assertEqual(expected.currency_code, actual.currency_code)
    self.assertEqual(expected.number_of_decimals, actual.number_of_decimals)
