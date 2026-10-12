# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class PaymentReferences(DataObject):

    __dynamic_descriptor: Optional[str] = None
    __merchant_reference: Optional[str] = None

    @property
    def dynamic_descriptor(self) -> Optional[str]:
        """
        | Custom text provided by the merchant that is shown to the customer on their account statement, next to or instead of the registered merchant name. Support and maximum length depend on the payment method.
        |
        | Note that there are restrictions on length and allowed characters that differ depending on the brand and scheme. If this string is too long it's usually truncated.

        Type: str
        """
        return self.__dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, value: Optional[str]) -> None:
        self.__dynamic_descriptor = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Custom text provided by the merchant that appears on their own settlement reports and on the reimbursement notices from the acquirer.
        |
        | It allows the merchant to reconcile their payments in our report files and in their disputes.
        |
        | It is advised to submit a unique value per transaction.
        | The value is returned in the baseTrxType/addlMercData element of the MRX file.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentReferences, self).to_dictionary()
        if self.dynamic_descriptor is not None:
            dictionary['dynamicDescriptor'] = self.dynamic_descriptor
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentReferences':
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'dynamicDescriptor' in dictionary:
            self.dynamic_descriptor = dictionary['dynamicDescriptor']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
