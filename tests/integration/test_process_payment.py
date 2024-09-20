import unittest

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import ACQUIRER_ID, MERCHANT_ID

from worldline.acquiring.sdk.v1.acquirer.merchant.payments.get_payment_status_params import GetPaymentStatusParams


class ProcessPaymentTest(unittest.TestCase):
    def test_process_payment(self):
        """Smoke test for process payment"""
        with init_utils.create_client() as client:
            payments_client = client.v1().acquirer(ACQUIRER_ID).merchant(MERCHANT_ID).payments()

            request = init_utils.get_api_payment_request()
            response = payments_client.process_payment(request)
            init_utils.assert_payment_response(self, request, response)

            payment_id = response.payment_id

            query = GetPaymentStatusParams()
            query.return_operations = True

            status = payments_client.get_payment_status(payment_id, query)
            init_utils.assert_payment_status_response(self, payment_id, status)


if __name__ == '__main__':
    unittest.main()
