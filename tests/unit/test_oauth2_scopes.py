import unittest

from worldline.acquiring.sdk.authentication.oauth2_scopes import OAuth2Scopes


class OAuth2ScopesTest(unittest.TestCase):

    def test_all(self):
        all_scopes = OAuth2Scopes.all()
        self.assertIn("processing_payment", all_scopes)
        self.assertIn("processing_dcc_rate", all_scopes)
        self.assertIn("services_ping", all_scopes)

        all_scopes_string = str.join(" ", all_scopes)
        self.assertLessEqual(len(all_scopes_string), 260, all_scopes_string + " is too long")

    def test_for_v1(self):
        scopes = OAuth2Scopes.for_api_version("v1")
        self.assertIn("processing_payment", scopes)
        self.assertIn("processing_dcc_rate", scopes)
        self.assertIn("services_ping", scopes)

    def test_for_unknown_api_version(self):
        scopes = OAuth2Scopes.for_api_version("v-1")
        self.assertEqual(set(), scopes)

    def test_for_v1_process_payment(self):
        scopes = OAuth2Scopes.for_operation("v1", "processPayment")
        self.assertIn("processing_payment", scopes)

    def test_for_v1_request_dcc_rate(self):
        scopes = OAuth2Scopes.for_operation("v1", "requestDccRate")
        self.assertIn("processing_dcc_rate", scopes)

    def test_for_unknown_operation(self):
        scopes = OAuth2Scopes.for_operation("v1", "unknown")
        self.assertEqual(set(), scopes)

    def test_for_operation_of_unknown_api_version(self):
        scopes = OAuth2Scopes.for_operation("v-1", "processPayment")
        self.assertEqual(set(), scopes)

    def test_for_v1_operations(self):
        scopes = OAuth2Scopes.for_operations("v1", "processPayment", "requestDccRate", "unknown")
        self.assertIn("processing_payment", scopes)
        self.assertIn("processing_dcc_rate", scopes)
        self.assertNotIn("services_ping", scopes)

    def test_for_operations_of_unknown_api_version(self):
        scopes = OAuth2Scopes.for_operations("v-1", "processPayment", "requestDccRate")
        self.assertEqual(set(), scopes)

    def test_for_filtered_operations(self):
        operation_ids = ["processPayment", "requestDccRate", "unknown"]
        scopes = OAuth2Scopes.for_filtered_operations(lambda v, o: v == "v1" and o in operation_ids)
        self.assertIn("processing_payment", scopes)
        self.assertIn("processing_dcc_rate", scopes)
        self.assertNotIn("services_ping", scopes)
