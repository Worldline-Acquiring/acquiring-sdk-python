# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .merchant_id_item import MerchantIdItem
from .merchant_scope import MerchantScope


class ByMerchantIds(MerchantScope):

    MERCHANT_SCOPE_TYPE = 'BY_MERCHANT_IDS'

    __merchant_ids: Optional[List[MerchantIdItem]] = None

    @property
    def merchant_scope_type(self) -> str:
        """
        | Possible values are: BY_ACQUIRER_IDS, BY_MERCHANT_ROOT_IDS, BY_MERCHANT_IDS.

        Type: str
        """
        return self.MERCHANT_SCOPE_TYPE

    @property
    def merchant_ids(self) -> Optional[List[MerchantIdItem]]:
        """
        Type: list[:class:`worldline.acquiring.sdk.v1.domain.merchant_id_item.MerchantIdItem`]
        """
        return self.__merchant_ids

    @merchant_ids.setter
    def merchant_ids(self, value: Optional[List[MerchantIdItem]]) -> None:
        self.__merchant_ids = value

    def to_dictionary(self) -> dict:
        dictionary = super(ByMerchantIds, self).to_dictionary()
        if self.merchant_ids is not None:
            dictionary['merchantIds'] = []
            for element in self.merchant_ids:
                if element is not None:
                    dictionary['merchantIds'].append(element.to_dictionary())
        dictionary['merchantScopeType'] = self.merchant_scope_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ByMerchantIds':
        super(ByMerchantIds, self).from_dictionary(dictionary)
        if 'merchantIds' in dictionary:
            if not isinstance(dictionary['merchantIds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['merchantIds']))
            self.merchant_ids = []
            for element in dictionary['merchantIds']:
                value = MerchantIdItem()
                self.merchant_ids.append(value.from_dictionary(element))
        return self
