from typing import Optional, Sequence
from urllib.parse import ParseResult

from worldline.acquiring.sdk.authentication.authenticator import Authenticator
from worldline.acquiring.sdk.communication.request_header import RequestHeader


class MockAuthenticator(Authenticator):
    def get_authorization(self, http_method: str, resource_uri: ParseResult,
                          request_headers: Optional[Sequence[RequestHeader]]) -> str:
        return 'Test'
