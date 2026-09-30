# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .merchant_scope import MerchantScope


class ByAcquirerIds(MerchantScope):

    MERCHANT_SCOPE_TYPE = 'BY_ACQUIRER_IDS'

    __acquirer_ids: Optional[List[str]] = None

    @property
    def merchant_scope_type(self) -> str:
        """
        | Possible values are: BY_ACQUIRER_IDS, BY_MERCHANT_ROOT_IDS, BY_MERCHANT_IDS.

        Type: str
        """
        return self.MERCHANT_SCOPE_TYPE

    @property
    def acquirer_ids(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__acquirer_ids

    @acquirer_ids.setter
    def acquirer_ids(self, value: Optional[List[str]]) -> None:
        self.__acquirer_ids = value

    def to_dictionary(self) -> dict:
        dictionary = super(ByAcquirerIds, self).to_dictionary()
        if self.acquirer_ids is not None:
            dictionary['acquirerIds'] = []
            for element in self.acquirer_ids:
                if element is not None:
                    dictionary['acquirerIds'].append(element)
        dictionary['merchantScopeType'] = self.merchant_scope_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ByAcquirerIds':
        super(ByAcquirerIds, self).from_dictionary(dictionary)
        if 'acquirerIds' in dictionary:
            if not isinstance(dictionary['acquirerIds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['acquirerIds']))
            self.acquirer_ids = []
            for element in dictionary['acquirerIds']:
                self.acquirer_ids.append(element)
        return self
