# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_data import AmountData

from worldline.acquiring.sdk.domain.data_object import DataObject


class CaptureAmountBreakdownData(DataObject):

    __tip_amount: Optional[AmountData] = None

    @property
    def tip_amount(self) -> Optional[AmountData]:
        """
        | Optional amount of tip.
        |
        | The amount specified is included in the total capture ``amount``, the information is provided for data enrichment and reconciliation purposes.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__tip_amount

    @tip_amount.setter
    def tip_amount(self, value: Optional[AmountData]) -> None:
        self.__tip_amount = value

    def to_dictionary(self) -> dict:
        dictionary = super(CaptureAmountBreakdownData, self).to_dictionary()
        if self.tip_amount is not None:
            dictionary['tipAmount'] = self.tip_amount.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CaptureAmountBreakdownData':
        super(CaptureAmountBreakdownData, self).from_dictionary(dictionary)
        if 'tipAmount' in dictionary:
            if not isinstance(dictionary['tipAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['tipAmount']))
            value = AmountData()
            self.tip_amount = value.from_dictionary(dictionary['tipAmount'])
        return self
