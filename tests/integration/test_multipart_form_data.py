"""
These tests verify the multipart/form-data requests that the SDK puts on the wire, using a local mock server.
"""
import io
import json
import queue
import re
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Dict, List, Optional
from urllib.parse import ParseResult

from worldline.acquiring.sdk.authentication.authenticator import Authenticator
from worldline.acquiring.sdk.communication.default_connection import DefaultConnection
from worldline.acquiring.sdk.communication.metadata_provider import MetadataProvider
from worldline.acquiring.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from worldline.acquiring.sdk.communication.multipart_form_data_request import MultipartFormDataRequest
from worldline.acquiring.sdk.communication.request_header import RequestHeader
from worldline.acquiring.sdk.communication.response_exception import ResponseException
from worldline.acquiring.sdk.communicator import Communicator
from worldline.acquiring.sdk.domain.data_object import DataObject
from worldline.acquiring.sdk.domain.uploadable_file import UploadableFile
from worldline.acquiring.sdk.json.default_marshaller import DefaultMarshaller

AUTHORIZATION = 'Bearer test-token'
REQUEST_TIMEOUT_SECONDS = 5


class MultipartFormDataTest(unittest.TestCase):
    """Test multipart/form-data uploads"""

    def setUp(self):
        self.server = MockHttpServer()
        self.server.start()
        self.addCleanup(self.server.stop)

        connection = DefaultConnection(5, 10)
        self.communicator = Communicator(self.server.url, connection, StubAuthenticator(), MetadataProvider('Worldline'),
                                         DefaultMarshaller.instance())
        self.addCleanup(self.communicator.close)

    def test_multipart_form_data_upload_post_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.post('/post', None, None, multipart, EchoResponse, None)

        self.assert_file_and_value_echoed(response.form, response.files)
        self.assert_file_and_value_request('POST', '/post', multipart)

    def test_multipart_form_data_upload_post_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data POST upload with a response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.post('/post', None, None, MultipartFormDataObjectWrapper(multipart), EchoResponse, None)

        self.assert_file_and_value_echoed(response.form, response.files)
        self.assert_file_and_value_request('POST', '/post', multipart)

    def test_multipart_form_data_upload_post_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.post_with_binary_response('/post', None, None, multipart, None)

        echo = read_binary_json_response(response)
        self.assert_file_and_value_echoed(echo['form'], echo['files'])
        self.assert_file_and_value_request('POST', '/post', multipart)

    def test_multipart_form_data_upload_post_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data POST upload with a binary response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.post_with_binary_response('/post', None, None, MultipartFormDataObjectWrapper(multipart), None)

        echo = read_binary_json_response(response)
        self.assert_file_and_value_echoed(echo['form'], echo['files'])
        self.assert_file_and_value_request('POST', '/post', multipart)

    def test_multipart_form_data_upload_put_multipart_form_data_object_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.put('/put', None, None, multipart, EchoResponse, None)

        self.assert_file_and_value_echoed(response.form, response.files)
        self.assert_file_and_value_request('PUT', '/put', multipart)

    def test_multipart_form_data_upload_put_multipart_form_data_request_with_response(self):
        """Test a multipart/form-data PUT upload with a response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.put('/put', None, None, MultipartFormDataObjectWrapper(multipart), EchoResponse, None)

        self.assert_file_and_value_echoed(response.form, response.files)
        self.assert_file_and_value_request('PUT', '/put', multipart)

    def test_multipart_form_data_upload_put_multipart_form_data_object_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.put_with_binary_response('/put', None, None, multipart, None)

        echo = read_binary_json_response(response)
        self.assert_file_and_value_echoed(echo['form'], echo['files'])
        self.assert_file_and_value_request('PUT', '/put', multipart)

    def test_multipart_form_data_upload_put_multipart_form_data_request_with_binary_response(self):
        """Test a multipart/form-data PUT upload with a binary response"""
        multipart = create_file_and_value_multipart()

        response = self.communicator.put_with_binary_response('/put', None, None, MultipartFormDataObjectWrapper(multipart), None)

        echo = read_binary_json_response(response)
        self.assert_file_and_value_echoed(echo['form'], echo['files'])
        self.assert_file_and_value_request('PUT', '/put', multipart)

    def test_multipart_form_data_upload_two_files(self):
        multipart = MultipartFormDataObject()
        multipart.add_file('firstFile', UploadableFile('first.txt', 'firstContent', 'text/plain'))
        multipart.add_file('secondFile', UploadableFile('second.txt', 'secondContent', 'text/plain'))

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(2, len(parts))
        self.assert_file_part(parts, 'firstFile', 'first.txt', 'text/plain', b'firstContent')
        self.assert_file_part(parts, 'secondFile', 'second.txt', 'text/plain', b'secondContent')

    def test_multipart_form_data_upload_three_files_with_different_types(self):
        multipart = MultipartFormDataObject()
        multipart.add_file('textFile', UploadableFile('file.txt', 'text', 'text/plain'))
        multipart.add_file('jsonFile', UploadableFile('file.json', '{"key": "json"}', 'application/json'))
        multipart.add_file('xmlFile', UploadableFile('file.xml', '<key>xml</key>', 'application/xml'))

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(3, len(parts))
        self.assert_file_part(parts, 'textFile', 'file.txt', 'text/plain', b'text')
        self.assert_file_part(parts, 'jsonFile', 'file.json', 'application/json', b'{"key": "json"}')
        self.assert_file_part(parts, 'xmlFile', 'file.xml', 'application/xml', b'<key>xml</key>')

    def test_multipart_form_data_upload_two_values(self):
        multipart = MultipartFormDataObject()
        multipart.add_value('firstKey', 'firstValue')
        multipart.add_value('secondKey', 'secondValue')

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(2, len(parts))
        self.assert_value_part(parts, 'firstKey', 'firstValue')
        self.assert_value_part(parts, 'secondKey', 'secondValue')

    def test_multipart_form_data_upload_three_values(self):
        multipart = MultipartFormDataObject()
        multipart.add_value('name', 'John')
        multipart.add_value('age', '30')
        multipart.add_value('city', 'NYC')

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(3, len(parts))
        self.assert_value_part(parts, 'name', 'John')
        self.assert_value_part(parts, 'age', '30')
        self.assert_value_part(parts, 'city', 'NYC')

    def test_multipart_form_data_upload_non_ascii_value(self):
        multipart = MultipartFormDataObject()
        multipart.add_value('greeting', 'Hello, Šđčćž €')

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(1, len(parts))
        self.assert_value_part(parts, 'greeting', 'Hello, Šđčćž €')

    def test_multipart_form_data_upload_single_file_without_values(self):
        multipart = MultipartFormDataObject()
        multipart.add_file('document', UploadableFile('doc.pdf', 'doc content', 'application/pdf'))

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(1, len(parts))
        self.assert_file_part(parts, 'document', 'doc.pdf', 'application/pdf', b'doc content')

    def test_multipart_form_data_upload_single_value_without_files(self):
        multipart = MultipartFormDataObject()
        multipart.add_value('message', 'Hello')

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(1, len(parts))
        self.assert_value_part(parts, 'message', 'Hello')

    def test_multipart_form_data_upload_content_types(self):
        for parameter_name, file_name, content_type, content in [
            ('pdf', 'document.pdf', 'application/pdf', 'pdf content'),
            ('image', 'photo.jpg', 'image/jpeg', 'image content'),
            ('data', 'data.json', 'application/json', '{"key": "value"}'),
        ]:
            with self.subTest(parameter_name=parameter_name):
                multipart = MultipartFormDataObject()
                multipart.add_file(parameter_name, UploadableFile(file_name, content, content_type))

                parts = self.post_and_take_parts(multipart)

                self.assertEqual(1, len(parts))
                self.assert_file_part(parts, parameter_name, file_name, content_type, content.encode('utf-8'))

    def test_multipart_form_data_upload_binary_file(self):
        content = bytes(i % 256 for i in range(64 * 1024))
        multipart = MultipartFormDataObject()
        multipart.add_file('binary', UploadableFile('data.bin', io.BytesIO(content), 'application/octet-stream'))

        parts = self.post_and_take_parts(multipart)

        self.assertEqual(1, len(parts))
        self.assert_file_part(parts, 'binary', 'data.bin', 'application/octet-stream', content)

    def test_multipart_form_data_upload_json_error_response(self):
        error_body = '{"status": 400, "title": "Bad Request"}'
        self.server.enqueue(MockResponse(400, 'application/json', error_body))

        multipart = MultipartFormDataObject()
        multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))

        with self.assertRaises(ResponseException) as context:
            self.communicator.post('/post', None, None, multipart, EchoResponse, None)

        self.assertEqual(400, context.exception.status_code)
        self.assertEqual(error_body, context.exception.body)

        parts = self.take_multipart_request('POST', '/post', multipart)
        self.assertEqual(1, len(parts))
        self.assert_file_part(parts, 'file', 'file.txt', 'text/plain', b'file-content')

    def post_and_take_parts(self, multipart: MultipartFormDataObject) -> Dict[str, 'MultipartPart']:
        response = self.communicator.post('/post', None, None, multipart, EchoResponse, None)
        self.assertIsNotNone(response)
        return self.take_multipart_request('POST', '/post', multipart)

    def take_multipart_request(self, expected_method: str, expected_path: str,
                               multipart: MultipartFormDataObject) -> Dict[str, 'MultipartPart']:
        """Verifies the request line and headers of the received multipart/form-data request, and returns its parts keyed by name"""
        request = self.server.take_request()
        self.assertIsNotNone(request, 'no request was received by the mock server')
        self.assertEqual(expected_method, request.method)
        self.assertEqual(expected_path, request.path)
        self.assertEqual(AUTHORIZATION, request.headers.get('Authorization'))
        self.assertEqual(multipart.content_type, request.headers.get('Content-Type'))
        return parse_multipart(request)

    def assert_file_and_value_echoed(self, form: Dict[str, str], files: Dict[str, str]):
        self.assertEqual({'value': 'Hello World'}, form)
        self.assertEqual({'file': 'file-content'}, files)

    def assert_file_and_value_request(self, expected_method: str, expected_path: str, multipart: MultipartFormDataObject):
        parts = self.take_multipart_request(expected_method, expected_path, multipart)
        self.assertEqual(2, len(parts))
        self.assert_file_part(parts, 'file', 'file.txt', 'text/plain', b'file-content')
        self.assert_value_part(parts, 'value', 'Hello World')

    def assert_file_part(self, parts: Dict[str, 'MultipartPart'], name: str, file_name: str, content_type: str, content: bytes):
        self.assertIn(name, parts)
        part = parts[name]
        self.assertEqual(file_name, part.file_name)
        self.assertEqual(content_type, part.headers.get('content-type'))
        self.assertEqual(content, part.content)

    def assert_value_part(self, parts: Dict[str, 'MultipartPart'], name: str, value: str):
        self.assertIn(name, parts)
        part = parts[name]
        self.assertIsNone(part.file_name, 'value part should not have a filename')
        self.assertEqual(value, part.content.decode('utf-8'))


def create_file_and_value_multipart() -> MultipartFormDataObject:
    multipart = MultipartFormDataObject()
    multipart.add_file('file', UploadableFile('file.txt', 'file-content', 'text/plain'))
    multipart.add_value('value', 'Hello World')
    return multipart


def read_binary_json_response(response) -> dict:
    data = b''
    for chunk in response[1]:
        data += chunk
    return json.loads(data.decode('utf-8'))


class StubAuthenticator(Authenticator):
    def get_authorization(self, http_method: str, resource_uri: ParseResult,
                          request_headers: Optional[List[RequestHeader]]) -> str:
        return AUTHORIZATION


class EchoResponse(DataObject):
    """The default response of the mock server"""
    method = None
    path = None
    form = None
    files = None

    def from_dictionary(self, dictionary):
        super(EchoResponse, self).from_dictionary(dictionary)
        for key in ('method', 'path', 'form', 'files'):
            if key in dictionary:
                setattr(self, key, dictionary[key])
        return self


class MultipartFormDataObjectWrapper(MultipartFormDataRequest):
    __multipart = None

    def __init__(self, multipart):
        self.__multipart = multipart

    def to_multipart_form_data_object(self):
        return self.__multipart


# mock server

class MockResponse(object):
    def __init__(self, status: int, content_type: str, body: str):
        self.status = status
        self.content_type = content_type
        self.body = body


class RecordedRequest(object):
    def __init__(self, method: str, path: str, headers, body: bytes):
        self.method = method
        self.path = path
        # an http.client.HTTPMessage; its get method is case-insensitive
        self.headers = headers
        self.body = body


class MultipartPart(object):
    def __init__(self, name: str, file_name: Optional[str], headers: Dict[str, str], content: bytes):
        self.name = name
        self.file_name = file_name
        # header names are lower-case
        self.headers = headers
        self.content = content


class MockHttpServer(object):

    def __init__(self):
        self.__requests = queue.Queue()
        self.__responses = queue.Queue()
        self.__server = ThreadingHTTPServer(('127.0.0.1', 0), _MockRequestHandler)
        self.__server.mock = self
        self.__thread = threading.Thread(target=self.__server.serve_forever, kwargs={'poll_interval': 0.1}, daemon=True)

    @property
    def url(self) -> str:
        return 'http://127.0.0.1:' + str(self.__server.server_address[1])

    def start(self):
        self.__thread.start()

    def stop(self):
        self.__server.shutdown()
        self.__server.server_close()

    def enqueue(self, response: MockResponse):
        self.__responses.put(response)

    def take_request(self) -> Optional[RecordedRequest]:
        """Returns the next received request, or None if no request is received within the timeout"""
        try:
            return self.__requests.get(timeout=REQUEST_TIMEOUT_SECONDS)
        except queue.Empty:
            return None

    def _handle(self, request: RecordedRequest) -> MockResponse:
        self.__requests.put(request)
        try:
            return self.__responses.get_nowait()
        except queue.Empty:
            return _create_echo_response(request)


class _MockRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.__handle()

    def do_POST(self):
        self.__handle()

    def do_PUT(self):
        self.__handle()

    def do_DELETE(self):
        self.__handle()

    def log_message(self, format, *args):
        # keep the test output clean
        pass

    def __handle(self):
        request = RecordedRequest(self.command, self.path, self.headers, self.__read_body())
        response = self.server.mock._handle(request)
        body = response.body.encode('utf-8')
        self.send_response(response.status)
        self.send_header('Content-Type', response.content_type)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def __read_body(self) -> bytes:
        if 'chunked' in self.headers.get('Transfer-Encoding', '').lower():
            body = b''
            while True:
                size = int(self.rfile.readline().split(b';')[0].strip(), 16)
                if size == 0:
                    # skip the (optional) trailers and the final empty line
                    while self.rfile.readline() not in (b'\r\n', b'\n', b''):
                        pass
                    return body
                body += self.rfile.read(size)
                self.rfile.readline()
        return self.rfile.read(int(self.headers.get('Content-Length', 0)))


def _create_echo_response(request: RecordedRequest) -> MockResponse:
    echo = {'method': request.method, 'path': request.path, 'form': {}, 'files': {}}
    if request.headers.get('Content-Type', '').lower().startswith('multipart/form-data'):
        try:
            for name, part in parse_multipart(request).items():
                target = echo['form'] if part.file_name is None else echo['files']
                target[name] = part.content.decode('utf-8', errors='replace')
        except ValueError as e:
            return MockResponse(400, 'application/json', json.dumps({'error': str(e)}))
    return MockResponse(200, 'application/json', json.dumps(echo))


def parse_multipart(request: RecordedRequest) -> Dict[str, MultipartPart]:
    """
    Parses the body of a multipart/form-data request into its parts, keyed by name.
    Each part is the content between two boundary delimiters: CRLF, headers, CRLF CRLF, content, CRLF.

    :raise ValueError: if the body is not a valid multipart/form-data body
    """
    content_type = request.headers.get('Content-Type', '')
    boundary_match = re.search(r';\s*boundary="?([^";]+)"?', content_type, re.IGNORECASE)
    if not boundary_match:
        raise ValueError('Content-Type has no boundary: ' + content_type)

    body = request.body
    delimiter = b'--' + boundary_match.group(1).encode('ascii')
    if not body.startswith(delimiter + b'\r\n'):
        raise ValueError('body does not start with the boundary delimiter')
    close_index = body.rfind(delimiter + b'--')
    if close_index < 0:
        raise ValueError('body does not contain the closing boundary delimiter')

    parts = {}
    # the first segment is the (empty) preamble before the first delimiter
    for segment in body[:close_index].split(delimiter)[1:]:
        if not segment.startswith(b'\r\n') or not segment.endswith(b'\r\n'):
            raise ValueError('part is not enclosed in CRLF')
        raw_part = segment[2:-2]
        header_end = raw_part.find(b'\r\n\r\n')
        if header_end < 0:
            raise ValueError('part has no header separator')

        headers = {}
        for header_line in raw_part[:header_end].decode('utf-8').split('\r\n'):
            name, separator, value = header_line.partition(':')
            if not separator or not name:
                raise ValueError('invalid part header: ' + header_line)
            headers[name.strip().lower()] = value.strip()

        content_disposition = headers.get('content-disposition', '')
        if not content_disposition.lower().startswith('form-data'):
            raise ValueError('unexpected Content-Disposition: ' + content_disposition)
        name_match = re.search(r';\s*name="([^"]*)"', content_disposition, re.IGNORECASE)
        if not name_match:
            raise ValueError('Content-Disposition has no name: ' + content_disposition)
        file_name_match = re.search(r';\s*filename="([^"]*)"', content_disposition, re.IGNORECASE)

        part_name = name_match.group(1)
        if part_name in parts:
            raise ValueError('duplicate part: ' + part_name)
        parts[part_name] = MultipartPart(part_name, file_name_match.group(1) if file_name_match else None, headers,
                                         raw_part[header_end + 4:])
    return parts


if __name__ == '__main__':
    unittest.main()
