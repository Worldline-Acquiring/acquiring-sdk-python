import unittest

from datetime import timedelta
from unittest.mock import Mock, MagicMock

from tests.unit.test_factory import PROPERTIES_URI_OAUTH2, OAUTH2_CLIENT_ID, OAUTH2_CLIENT_SECRET

from worldline.acquiring.sdk.factory import Factory
from worldline.acquiring.sdk.communication.connection import Connection
from worldline.acquiring.sdk.communication.pooled_connection import PooledConnection


class ClientTest(unittest.TestCase):
    """Tests for the Client class testing if connection settings are propagated properly to the connection object
    """

    def test_close_idle_connection_not_pooled(self):
        """Tests that the setting to close an idle connection in a client propagates to the connection
        for an unpooled connection
        """
        mock = MagicMock(spec=Connection, autospec=True)
        function_mock = Mock(name="close_idle_connections_mock")
        mock.attach_mock(function_mock, "close_idle_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI_OAUTH2,
                                                             authorization_id=OAUTH2_CLIENT_ID, authorization_secret=OAUTH2_CLIENT_SECRET,
                                                             connection=mock)
        client = Factory.create_client_from_communicator(communicator)

        client.close_idle_connections(timedelta(seconds=5))  # seconds

        function_mock.assert_not_called()

    def test_close_idle_connection_pooled(self):
        """Tests that the setting to close an idle connection in a client propagates to the connection
            for a pooled connection
            """
        pooled_mock = MagicMock(spec=PooledConnection, autospec=True)
        function_mock = Mock(name="close_idle_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_idle_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI_OAUTH2,
                                                             authorization_id=OAUTH2_CLIENT_ID, authorization_secret=OAUTH2_CLIENT_SECRET,
                                                             connection=pooled_mock)
        client = Factory.create_client_from_communicator(communicator)

        client.close_idle_connections(timedelta(seconds=5))  # seconds

        function_mock.assert_called_once_with(timedelta(seconds=5))

    def test_close_expired_connections_not_pooled(self):
        """Tests that the setting to close an expired connection in a client does not propagate to the connection
        for an unpooled connection
        """
        mock = MagicMock(spec=Connection, autospec=True)
        function_mock = Mock(name="close_expired_connections_mock")
        mock.attach_mock(function_mock, "close_expired_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI_OAUTH2,
                                                             authorization_id=OAUTH2_CLIENT_ID, authorization_secret=OAUTH2_CLIENT_SECRET,
                                                             connection=mock)
        client = Factory.create_client_from_communicator(communicator)

        client.close_expired_connections()

        function_mock.assert_not_called()

    def test_close_expired_connections_pooled(self):
        """Tests that the setting to close an expired connection in a client propagates to the connection
        for a pooled connection
        """
        pooled_mock = MagicMock(spec=PooledConnection, autospec=True)
        function_mock = Mock(name="close_expired_connections_mock")
        pooled_mock.attach_mock(function_mock, "close_expired_connections")
        communicator = Factory.create_communicator_from_file(configuration_file_name=PROPERTIES_URI_OAUTH2,
                                                             authorization_id=OAUTH2_CLIENT_ID, authorization_secret=OAUTH2_CLIENT_SECRET,
                                                             connection=pooled_mock)
        client = Factory.create_client_from_communicator(communicator)

        client.close_expired_connections()

        function_mock.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
