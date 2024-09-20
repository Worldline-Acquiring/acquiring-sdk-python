# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .api_payment_summary_for_response import ApiPaymentSummaryForResponse

from worldline.acquiring.sdk.domain.data_object import DataObject


class ApiActionResponse(DataObject):

    __operation_id: Optional[str] = None
    __payment: Optional[ApiPaymentSummaryForResponse] = None
    __responder: Optional[str] = None
    __response_code: Optional[str] = None
    __response_code_category: Optional[str] = None
    __response_code_description: Optional[str] = None

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
    def payment(self) -> Optional[ApiPaymentSummaryForResponse]:
        """
        | A summary of the payment used for responses

        Type: :class:`worldline.acquiring.sdk.v1.domain.api_payment_summary_for_response.ApiPaymentSummaryForResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value: Optional[ApiPaymentSummaryForResponse]) -> None:
        self.__payment = value

    @property
    def responder(self) -> Optional[str]:
        """
        | The party that originated the response

        Type: str
        """
        return self.__responder

    @responder.setter
    def responder(self, value: Optional[str]) -> None:
        self.__responder = value

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

    def to_dictionary(self) -> dict:
        dictionary = super(ApiActionResponse, self).to_dictionary()
        if self.operation_id is not None:
            dictionary['operationId'] = self.operation_id
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        if self.responder is not None:
            dictionary['responder'] = self.responder
        if self.response_code is not None:
            dictionary['responseCode'] = self.response_code
        if self.response_code_category is not None:
            dictionary['responseCodeCategory'] = self.response_code_category
        if self.response_code_description is not None:
            dictionary['responseCodeDescription'] = self.response_code_description
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ApiActionResponse':
        super(ApiActionResponse, self).from_dictionary(dictionary)
        if 'operationId' in dictionary:
            self.operation_id = dictionary['operationId']
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = ApiPaymentSummaryForResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        if 'responder' in dictionary:
            self.responder = dictionary['responder']
        if 'responseCode' in dictionary:
            self.response_code = dictionary['responseCode']
        if 'responseCodeCategory' in dictionary:
            self.response_code_category = dictionary['responseCodeCategory']
        if 'responseCodeDescription' in dictionary:
            self.response_code_description = dictionary['responseCodeDescription']
        return self
