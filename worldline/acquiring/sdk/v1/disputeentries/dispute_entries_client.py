# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from worldline.acquiring.sdk.api_resource import ApiResource
from worldline.acquiring.sdk.call_context import CallContext
from worldline.acquiring.sdk.communication.response_exception import ResponseException
from worldline.acquiring.sdk.v1.domain.api_payment_error_response import ApiPaymentErrorResponse
from worldline.acquiring.sdk.v1.domain.dispute_entry_resources import DisputeEntryResources
from worldline.acquiring.sdk.v1.domain.search_dispute_entries_request import SearchDisputeEntriesRequest
from worldline.acquiring.sdk.v1.exception_factory import create_exception


class DisputeEntriesClient(ApiResource):
    """
    DisputeEntries client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`worldline.acquiring.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(DisputeEntriesClient, self).__init__(parent=parent, path_context=path_context)

    def search_dispute_entries(self, body: SearchDisputeEntriesRequest, context: Optional[CallContext] = None) -> DisputeEntryResources:
        """
        Resource /dispute-management/v1/dispute-entries/search - Search Dispute Entries

        See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Entries/operation/searchDisputeEntries

        :param body:     :class:`worldline.acquiring.sdk.v1.domain.search_dispute_entries_request.SearchDisputeEntriesRequest`
        :param context:  :class:`worldline.acquiring.sdk.call_context.CallContext`
        :return: :class:`worldline.acquiring.sdk.v1.domain.dispute_entry_resources.DisputeEntryResources`
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the Worldline Acquiring platform,
                   the Worldline Acquiring platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the Worldline Acquiring platform returned any other error
        """
        uri = self._instantiate_uri("/dispute-management/v1/dispute-entries/search", None)
        try:
            return self._communicator.post(
                    uri,
                    None,
                    None,
                    body,
                    DisputeEntryResources,
                    context)

        except ResponseException as e:
            error_type = ApiPaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)
