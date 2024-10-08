# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class PaymentReferences(DataObject):

    __dynamic_descriptor: Optional[str] = None
    __merchant_reference: Optional[str] = None
    __retrieval_reference_number: Optional[str] = None

    @property
    def dynamic_descriptor(self) -> Optional[str]:
        """
        | Dynamic descriptor gives you the ability to control the descriptor on the credit card statement of the customer.

        Type: str
        """
        return self.__dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, value: Optional[str]) -> None:
        self.__dynamic_descriptor = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Reference for the transaction to allow the merchant to reconcile their payments in our report files.
        | It is advised to submit a unique value per transaction.
        | The value provided here is returned in the baseTrxType/addlMercData element of the MRX file.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    @property
    def retrieval_reference_number(self) -> Optional[str]:
        """
        | Retrieval reference number for transaction, must be AN(12) if provided

        Type: str
        """
        return self.__retrieval_reference_number

    @retrieval_reference_number.setter
    def retrieval_reference_number(self, value: Optional[str]) -> None:
        self.__retrieval_reference_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentReferences, self).to_dictionary()
        if self.dynamic_descriptor is not None:
            dictionary['dynamicDescriptor'] = self.dynamic_descriptor
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.retrieval_reference_number is not None:
            dictionary['retrievalReferenceNumber'] = self.retrieval_reference_number
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentReferences':
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'dynamicDescriptor' in dictionary:
            self.dynamic_descriptor = dictionary['dynamicDescriptor']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'retrievalReferenceNumber' in dictionary:
            self.retrieval_reference_number = dictionary['retrievalReferenceNumber']
        return self
