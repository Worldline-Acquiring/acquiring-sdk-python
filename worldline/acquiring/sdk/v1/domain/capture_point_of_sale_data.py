# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .emv_data_item import EmvDataItem

from worldline.acquiring.sdk.domain.data_object import DataObject


class CapturePointOfSaleData(DataObject):

    __emv_data: Optional[List[EmvDataItem]] = None

    @property
    def emv_data(self) -> Optional[List[EmvDataItem]]:
        """
        | EMV data of the card as tag/value pairs.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.emv_data_item.EmvDataItem`]
        """
        return self.__emv_data

    @emv_data.setter
    def emv_data(self, value: Optional[List[EmvDataItem]]) -> None:
        self.__emv_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(CapturePointOfSaleData, self).to_dictionary()
        if self.emv_data is not None:
            dictionary['emvData'] = []
            for element in self.emv_data:
                if element is not None:
                    dictionary['emvData'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CapturePointOfSaleData':
        super(CapturePointOfSaleData, self).from_dictionary(dictionary)
        if 'emvData' in dictionary:
            if not isinstance(dictionary['emvData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['emvData']))
            self.emv_data = []
            for element in dictionary['emvData']:
                value = EmvDataItem()
                self.emv_data.append(value.from_dictionary(element))
        return self
