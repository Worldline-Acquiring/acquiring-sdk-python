import unittest

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import ACQUIRER_ID, MERCHANT_ID


class ProcessPaymentTest(unittest.TestCase):
    def test_request_dcc_rate(self):
        """Smoke test for request DCC rate"""
        with init_utils.create_client() as client:
            request = init_utils.get_dcc_rate_request()
            response = client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).dynamic_currency_conversion().request_dcc_rate(request)
            init_utils.assert_dcc_rate_response(self, request, response)


if __name__ == '__main__':
    unittest.main()
