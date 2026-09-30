# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeMerchantDataBase(DataObject):

    __acquirer_id: Optional[str] = None
    __merchant_id: Optional[str] = None
    __merchant_root_id: Optional[str] = None

    @property
    def acquirer_id(self) -> Optional[str]:
        """
        | The unique identifier of the acquirer.

        Type: str
        """
        return self.__acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, value: Optional[str]) -> None:
        self.__acquirer_id = value

    @property
    def merchant_id(self) -> Optional[str]:
        """
        | The unique identifier of the merchant.

        Type: str
        """
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value: Optional[str]) -> None:
        self.__merchant_id = value

    @property
    def merchant_root_id(self) -> Optional[str]:
        """
        | The root identifier of the merchant, which is the same for all sub-merchants under the same parent company.

        Type: str
        """
        return self.__merchant_root_id

    @merchant_root_id.setter
    def merchant_root_id(self, value: Optional[str]) -> None:
        self.__merchant_root_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeMerchantDataBase, self).to_dictionary()
        if self.acquirer_id is not None:
            dictionary['acquirerId'] = self.acquirer_id
        if self.merchant_id is not None:
            dictionary['merchantId'] = self.merchant_id
        if self.merchant_root_id is not None:
            dictionary['merchantRootId'] = self.merchant_root_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeMerchantDataBase':
        super(DisputeMerchantDataBase, self).from_dictionary(dictionary)
        if 'acquirerId' in dictionary:
            self.acquirer_id = dictionary['acquirerId']
        if 'merchantId' in dictionary:
            self.merchant_id = dictionary['merchantId']
        if 'merchantRootId' in dictionary:
            self.merchant_root_id = dictionary['merchantRootId']
        return self
