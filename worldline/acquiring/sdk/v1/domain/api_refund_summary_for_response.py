# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .api_references_for_responses import ApiReferencesForResponses

from worldline.acquiring.sdk.domain.data_object import DataObject


class ApiRefundSummaryForResponse(DataObject):

    __references: Optional[ApiReferencesForResponses] = None
    __refund_id: Optional[str] = None
    __retry_after: Optional[str] = None
    __status: Optional[str] = None
    __status_timestamp: Optional[datetime] = None

    @property
    def references(self) -> Optional[ApiReferencesForResponses]:
        """
        | A set of references returned in responses

        Type: :class:`worldline.acquiring.sdk.v1.domain.api_references_for_responses.ApiReferencesForResponses`
        """
        return self.__references

    @references.setter
    def references(self, value: Optional[ApiReferencesForResponses]) -> None:
        self.__references = value

    @property
    def refund_id(self) -> Optional[str]:
        """
        | the ID of the refund

        Type: str
        """
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value: Optional[str]) -> None:
        self.__refund_id = value

    @property
    def retry_after(self) -> Optional[str]:
        """
        | The duration to wait after the initial submission before retrying the payment.
        | Expressed using ISO 8601 duration format, ex: PT2H for 2 hours.
        | This field is only present when the payment can be retried later.
        | PT0 means that the payment can be retried immediately.

        Type: str
        """
        return self.__retry_after

    @retry_after.setter
    def retry_after(self, value: Optional[str]) -> None:
        self.__retry_after = value

    @property
    def status(self) -> Optional[str]:
        """
        | The status of the payment, refund or credit transfer

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value: Optional[str]) -> None:
        self.__status = value

    @property
    def status_timestamp(self) -> Optional[datetime]:
        """
        | Timestamp of the status in format yyyy-MM-ddTHH:mm:ssZ

        Type: datetime
        """
        return self.__status_timestamp

    @status_timestamp.setter
    def status_timestamp(self, value: Optional[datetime]) -> None:
        self.__status_timestamp = value

    def to_dictionary(self) -> dict:
        dictionary = super(ApiRefundSummaryForResponse, self).to_dictionary()
        if self.references is not None:
            dictionary['references'] = self.references.to_dictionary()
        if self.refund_id is not None:
            dictionary['refundId'] = self.refund_id
        if self.retry_after is not None:
            dictionary['retryAfter'] = self.retry_after
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_timestamp is not None:
            dictionary['statusTimestamp'] = DataObject.format_datetime(self.status_timestamp)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApiRefundSummaryForResponse':
        super(ApiRefundSummaryForResponse, self).from_dictionary(dictionary)
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = ApiReferencesForResponses()
            self.references = value.from_dictionary(dictionary['references'])
        if 'refundId' in dictionary:
            self.refund_id = dictionary['refundId']
        if 'retryAfter' in dictionary:
            self.retry_after = dictionary['retryAfter']
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusTimestamp' in dictionary:
            self.status_timestamp = DataObject.parse_datetime(dictionary['statusTimestamp'])
        return self
