# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional, cast

from worldline.acquiring.sdk.domain.data_object import DataObject


class MerchantScope(DataObject):

    __merchant_scope_type: Optional[str] = None

    @property
    def merchant_scope_type(self) -> str:
        """
        | Possible values are: BY_ACQUIRER_IDS, BY_MERCHANT_ROOT_IDS, BY_MERCHANT_IDS.

        Type: str
        """
        return cast(str, self.__merchant_scope_type)

    @merchant_scope_type.setter
    def merchant_scope_type(self, value: str) -> None:
        self.__merchant_scope_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(MerchantScope, self).to_dictionary()
        if self.merchant_scope_type is not None:
            dictionary['merchantScopeType'] = self.merchant_scope_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MerchantScope':
        super(MerchantScope, self).from_dictionary(dictionary)
        if 'merchantScopeType' in dictionary:
            self.__merchant_scope_type = dictionary['merchantScopeType']
        return self
