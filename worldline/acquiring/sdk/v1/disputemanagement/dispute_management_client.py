# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Mapping, Optional

from .get_dispute_params import GetDisputeParams

from worldline.acquiring.sdk.api_resource import ApiResource
from worldline.acquiring.sdk.call_context import CallContext
from worldline.acquiring.sdk.communication.response_exception import ResponseException
from worldline.acquiring.sdk.v1.domain.accept_dispute_liability_request import AcceptDisputeLiabilityRequest
from worldline.acquiring.sdk.v1.domain.api_payment_error_response import ApiPaymentErrorResponse
from worldline.acquiring.sdk.v1.domain.dispute_response import DisputeResponse
from worldline.acquiring.sdk.v1.domain.search_disputes_request import SearchDisputesRequest
from worldline.acquiring.sdk.v1.domain.search_disputes_response import SearchDisputesResponse
from worldline.acquiring.sdk.v1.domain.submit_evidence_request import SubmitEvidenceRequest
from worldline.acquiring.sdk.v1.exception_factory import create_exception


class DisputeManagementClient(ApiResource):
    """
    DisputeManagement client. Thread-safe.
    """

    def __init__(self, parent: ApiResource, path_context: Optional[Mapping[str, str]]):
        """
        :param parent:       :class:`worldline.acquiring.sdk.api_resource.ApiResource`
        :param path_context: Mapping[str, str]
        """
        super(DisputeManagementClient, self).__init__(parent=parent, path_context=path_context)

    def search_disputes(self, body: SearchDisputesRequest, context: Optional[CallContext] = None) -> SearchDisputesResponse:
        """
        Resource /dispute-management/v1/disputes/search - Search Disputes

        See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Management/operation/searchDisputes

        :param body:     :class:`worldline.acquiring.sdk.v1.domain.search_disputes_request.SearchDisputesRequest`
        :param context:  :class:`worldline.acquiring.sdk.call_context.CallContext`
        :return: :class:`worldline.acquiring.sdk.v1.domain.search_disputes_response.SearchDisputesResponse`
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the Worldline Acquiring platform,
                   the Worldline Acquiring platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the Worldline Acquiring platform returned any other error
        """
        uri = self._instantiate_uri("/dispute-management/v1/disputes/search", None)
        try:
            return self._communicator.post(
                    uri,
                    None,
                    None,
                    body,
                    SearchDisputesResponse,
                    context)

        except ResponseException as e:
            error_type = ApiPaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def get_dispute(self, dispute_id: str, query: GetDisputeParams, context: Optional[CallContext] = None) -> DisputeResponse:
        """
        Resource /dispute-management/v1/disputes/{disputeId} - Retrieve Dispute

        See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Management/operation/getDispute

        :param dispute_id:  str
        :param query:       :class:`worldline.acquiring.sdk.v1.disputemanagement.get_dispute_params.GetDisputeParams`
        :param context:     :class:`worldline.acquiring.sdk.call_context.CallContext`
        :return: :class:`worldline.acquiring.sdk.v1.domain.dispute_response.DisputeResponse`
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the Worldline Acquiring platform,
                   the Worldline Acquiring platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the Worldline Acquiring platform returned any other error
        """
        path_context = {
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/dispute-management/v1/disputes/{disputeId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    None,
                    query,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ApiPaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def accept_dispute_liability(self, dispute_id: str, body: AcceptDisputeLiabilityRequest, context: Optional[CallContext] = None) -> DisputeResponse:
        """
        Resource /dispute-management/v1/disputes/{disputeId}/accept - Accept Liability

        See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Management/operation/acceptDisputeLiability

        :param dispute_id:  str
        :param body:        :class:`worldline.acquiring.sdk.v1.domain.accept_dispute_liability_request.AcceptDisputeLiabilityRequest`
        :param context:     :class:`worldline.acquiring.sdk.call_context.CallContext`
        :return: :class:`worldline.acquiring.sdk.v1.domain.dispute_response.DisputeResponse`
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the Worldline Acquiring platform,
                   the Worldline Acquiring platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the Worldline Acquiring platform returned any other error
        """
        path_context = {
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/dispute-management/v1/disputes/{disputeId}/accept", path_context)
        try:
            return self._communicator.post(
                    uri,
                    None,
                    None,
                    body,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ApiPaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)

    def submit_evidence(self, dispute_id: str, body: SubmitEvidenceRequest, context: Optional[CallContext] = None) -> DisputeResponse:
        """
        Resource /dispute-management/v1/disputes/{disputeId}/submit-evidence - Submit Evidence

        See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Management/operation/submitEvidence

        :param dispute_id:  str
        :param body:        :class:`worldline.acquiring.sdk.v1.domain.submit_evidence_request.SubmitEvidenceRequest`
        :param context:     :class:`worldline.acquiring.sdk.call_context.CallContext`
        :return: :class:`worldline.acquiring.sdk.v1.domain.dispute_response.DisputeResponse`
        :raise ValidationException: if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise AuthorizationException: if the request was not allowed (HTTP status code 403)
        :raise ReferenceException: if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise PlatformException: if something went wrong at the Worldline Acquiring platform,
                   the Worldline Acquiring platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise ApiException: if the Worldline Acquiring platform returned any other error
        """
        path_context = {
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/dispute-management/v1/disputes/{disputeId}/submit-evidence", path_context)
        try:
            return self._communicator.post(
                    uri,
                    None,
                    None,
                    body,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ApiPaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise create_exception(e.status_code, e.body, error_object, context)
