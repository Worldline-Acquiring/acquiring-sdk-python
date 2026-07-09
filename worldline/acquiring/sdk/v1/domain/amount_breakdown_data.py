# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_data import AmountData

from worldline.acquiring.sdk.domain.data_object import DataObject


class AmountBreakdownData(DataObject):

    __cashback_amount: Optional[AmountData] = None
    __tip_amount: Optional[AmountData] = None

    @property
    def cashback_amount(self) -> Optional[AmountData]:
        """
        | Optional amount of cashback for card-present transactions.
        |
        | The amount specified is included in the total transaction ``amount``, the information is provided for data enrichment and reconciliation purposes.
        |
        | Only supported in some regions with restrictions, depending on local regulation and card scheme rules. Please check with your Worldline contact if you are allowed to use this field.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__cashback_amount

    @cashback_amount.setter
    def cashback_amount(self, value: Optional[AmountData]) -> None:
        self.__cashback_amount = value

    @property
    def tip_amount(self) -> Optional[AmountData]:
        """
        | Optional amount of tip.
        |
        | The amount specified is included in the total transaction ``amount``, the information is provided for data enrichment and reconciliation purposes.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__tip_amount

    @tip_amount.setter
    def tip_amount(self, value: Optional[AmountData]) -> None:
        self.__tip_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(AmountBreakdownData, self).to_dictionary()
        if self.cashback_amount is not None:
            dictionary['cashbackAmount'] = self.cashback_amount.to_dictionary()
        if self.tip_amount is not None:
            dictionary['tipAmount'] = self.tip_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AmountBreakdownData':
        super(AmountBreakdownData, self).from_dictionary(dictionary)
        if 'cashbackAmount' in dictionary:
            if not isinstance(dictionary['cashbackAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cashbackAmount']))
            value = AmountData()
            self.cashback_amount = value.from_dictionary(dictionary['cashbackAmount'])
        if 'tipAmount' in dictionary:
            if not isinstance(dictionary['tipAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['tipAmount']))
            value = AmountData()
            self.tip_amount = value.from_dictionary(dictionary['tipAmount'])
        return self
