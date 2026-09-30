# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class TransactionReferencesBase(DataObject):

    __acquirer_reference_number: Optional[str] = None
    __merchant_reference: Optional[str] = None
    __payment_id: Optional[str] = None

    @property
    def acquirer_reference_number(self) -> Optional[str]:
        """
        | Acquirer reference number (ARN) for transaction

        Type: str
        """
        return self.__acquirer_reference_number

    @acquirer_reference_number.setter
    def acquirer_reference_number(self, value: Optional[str]) -> None:
        self.__acquirer_reference_number = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Reference for the transaction to allow the merchant to reconcile their payments in our report files and in their disputes.
        | It is advised to submit a unique value per transaction.
        | The value is returned in the baseTrxType/addlMercData element of the MRX file.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    @property
    def payment_id(self) -> Optional[str]:
        """
        | The unique identifier for the original payment transaction that resulted in the dispute. Depending on the interface used for the original transaction different values are returned. If the original transaction was made through the Acquiring API, the ``paymentId`` from the original transaction is returned.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(TransactionReferencesBase, self).to_dictionary()
        if self.acquirer_reference_number is not None:
            dictionary['acquirerReferenceNumber'] = self.acquirer_reference_number
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'TransactionReferencesBase':
        super(TransactionReferencesBase, self).from_dictionary(dictionary)
        if 'acquirerReferenceNumber' in dictionary:
            self.acquirer_reference_number = dictionary['acquirerReferenceNumber']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        return self
