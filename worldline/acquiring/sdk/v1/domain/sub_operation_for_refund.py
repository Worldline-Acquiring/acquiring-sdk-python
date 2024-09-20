# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import datetime
from typing import Optional

from .amount_data import AmountData

from worldline.acquiring.sdk.domain.data_object import DataObject


class SubOperationForRefund(DataObject):

    __amount: Optional[AmountData] = None
    __operation_id: Optional[str] = None
    __operation_timestamp: Optional[datetime] = None
    __operation_type: Optional[str] = None
    __response_code: Optional[str] = None
    __response_code_category: Optional[str] = None
    __response_code_description: Optional[str] = None
    __retry_after: Optional[str] = None

    @property
    def amount(self) -> Optional[AmountData]:
        """
        | Amount for the operation.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__amount

    @amount.setter
    def amount(self, value: Optional[AmountData]) -> None:
        self.__amount = value

    @property
    def operation_id(self) -> Optional[str]:
        """
        | A globally unique identifier of the operation, generated by you.
        | We advise you to submit a UUID or an identifier composed of an arbitrary string and a UUID/URL-safe Base64 UUID (RFC 4648 §5).
        | It's used to detect duplicate requests or to reference an operation in technical reversals.

        Type: str
        """
        return self.__operation_id

    @operation_id.setter
    def operation_id(self, value: Optional[str]) -> None:
        self.__operation_id = value

    @property
    def operation_timestamp(self) -> Optional[datetime]:
        """
        | Timestamp of the operation in merchant time zone in format yyyy-MM-ddTHH:mm:ssZ

        Type: datetime
        """
        return self.__operation_timestamp

    @operation_timestamp.setter
    def operation_timestamp(self, value: Optional[datetime]) -> None:
        self.__operation_timestamp = value

    @property
    def operation_type(self) -> Optional[str]:
        """
        | The kind of operation

        Type: str
        """
        return self.__operation_type

    @operation_type.setter
    def operation_type(self, value: Optional[str]) -> None:
        self.__operation_type = value

    @property
    def response_code(self) -> Optional[str]:
        """
        | Numeric response code, e.g. 0000, 0005

        Type: str
        """
        return self.__response_code

    @response_code.setter
    def response_code(self, value: Optional[str]) -> None:
        self.__response_code = value

    @property
    def response_code_category(self) -> Optional[str]:
        """
        | Category of response code.

        Type: str
        """
        return self.__response_code_category

    @response_code_category.setter
    def response_code_category(self, value: Optional[str]) -> None:
        self.__response_code_category = value

    @property
    def response_code_description(self) -> Optional[str]:
        """
        | Description of the response code

        Type: str
        """
        return self.__response_code_description

    @response_code_description.setter
    def response_code_description(self, value: Optional[str]) -> None:
        self.__response_code_description = value

    @property
    def retry_after(self) -> Optional[str]:
        """
        | The duration to wait after the initial submission before retrying the operation.
        | Expressed using ISO 8601 duration format, ex: PT2H for 2 hours.
        | This field is only present when the operation can be retried later.
        | PT0 means that the operation can be retried immediately.

        Type: str
        """
        return self.__retry_after

    @retry_after.setter
    def retry_after(self, value: Optional[str]) -> None:
        self.__retry_after = value

    def to_dictionary(self) -> dict:
        dictionary = super(SubOperationForRefund, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount.to_dictionary()
        if self.operation_id is not None:
            dictionary['operationId'] = self.operation_id
        if self.operation_timestamp is not None:
            dictionary['operationTimestamp'] = DataObject.format_datetime(self.operation_timestamp)
        if self.operation_type is not None:
            dictionary['operationType'] = self.operation_type
        if self.response_code is not None:
            dictionary['responseCode'] = self.response_code
        if self.response_code_category is not None:
            dictionary['responseCodeCategory'] = self.response_code_category
        if self.response_code_description is not None:
            dictionary['responseCodeDescription'] = self.response_code_description
        if self.retry_after is not None:
            dictionary['retryAfter'] = self.retry_after
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubOperationForRefund':
        super(SubOperationForRefund, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            if not isinstance(dictionary['amount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amount']))
            value = AmountData()
            self.amount = value.from_dictionary(dictionary['amount'])
        if 'operationId' in dictionary:
            self.operation_id = dictionary['operationId']
        if 'operationTimestamp' in dictionary:
            self.operation_timestamp = DataObject.parse_datetime(dictionary['operationTimestamp'])
        if 'operationType' in dictionary:
            self.operation_type = dictionary['operationType']
        if 'responseCode' in dictionary:
            self.response_code = dictionary['responseCode']
        if 'responseCodeCategory' in dictionary:
            self.response_code_category = dictionary['responseCodeCategory']
        if 'responseCodeDescription' in dictionary:
            self.response_code_description = dictionary['responseCodeDescription']
        if 'retryAfter' in dictionary:
            self.retry_after = dictionary['retryAfter']
        return self
