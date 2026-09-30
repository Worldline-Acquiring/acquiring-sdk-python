# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .merchant_root_id_item import MerchantRootIdItem
from .merchant_scope import MerchantScope


class ByMerchantRootIds(MerchantScope):

    MERCHANT_SCOPE_TYPE = 'BY_MERCHANT_ROOT_IDS'

    __merchant_root_ids: Optional[List[MerchantRootIdItem]] = None

    @property
    def merchant_scope_type(self) -> str:
        """
        | Possible values are: BY_ACQUIRER_IDS, BY_MERCHANT_ROOT_IDS, BY_MERCHANT_IDS.

        Type: str
        """
        return self.MERCHANT_SCOPE_TYPE

    @property
    def merchant_root_ids(self) -> Optional[List[MerchantRootIdItem]]:
        """
        Type: list[:class:`worldline.acquiring.sdk.v1.domain.merchant_root_id_item.MerchantRootIdItem`]
        """
        return self.__merchant_root_ids

    @merchant_root_ids.setter
    def merchant_root_ids(self, value: Optional[List[MerchantRootIdItem]]) -> None:
        self.__merchant_root_ids = value

    def to_dictionary(self) -> dict:
        dictionary = super(ByMerchantRootIds, self).to_dictionary()
        if self.merchant_root_ids is not None:
            dictionary['merchantRootIds'] = []
            for element in self.merchant_root_ids:
                if element is not None:
                    dictionary['merchantRootIds'].append(element.to_dictionary())
        dictionary['merchantScopeType'] = self.merchant_scope_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ByMerchantRootIds':
        super(ByMerchantRootIds, self).from_dictionary(dictionary)
        if 'merchantRootIds' in dictionary:
            if not isinstance(dictionary['merchantRootIds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['merchantRootIds']))
            self.merchant_root_ids = []
            for element in dictionary['merchantRootIds']:
                value = MerchantRootIdItem()
                self.merchant_root_ids.append(value.from_dictionary(element))
        return self
