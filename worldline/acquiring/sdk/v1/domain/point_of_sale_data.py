# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .emv_data_item import EmvDataItem
from .online_pin_data import OnlinePinData

from worldline.acquiring.sdk.domain.data_object import DataObject


class PointOfSaleData(DataObject):

    __emv_data: Optional[List[EmvDataItem]] = None
    __is_response_to_pin_request: Optional[bool] = None
    __is_retry_with_the_same_operation_id: Optional[bool] = None
    __online_pin_data: Optional[OnlinePinData] = None
    __track2_data: Optional[str] = None

    @property
    def emv_data(self) -> Optional[List[EmvDataItem]]:
        """
        | EMV data of the card as tag/value pairs.
        | It is needed when cardEntryMode is CHIP or CONTACTLESS.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.emv_data_item.EmvDataItem`]
        """
        return self.__emv_data

    @emv_data.setter
    def emv_data(self, value: Optional[List[EmvDataItem]]) -> None:
        self.__emv_data = value

    @property
    def is_response_to_pin_request(self) -> Optional[bool]:
        """
        | Indicate whether the request is made after a first one that resulted in a PIN request

        Type: bool
        """
        return self.__is_response_to_pin_request

    @is_response_to_pin_request.setter
    def is_response_to_pin_request(self, value: Optional[bool]) -> None:
        self.__is_response_to_pin_request = value

    @property
    def is_retry_with_the_same_operation_id(self) -> Optional[bool]:
        """
        | Indicate whether the request is a retry with the same operation ID after a first request that resulted in a PIN request

        Type: bool
        """
        return self.__is_retry_with_the_same_operation_id

    @is_retry_with_the_same_operation_id.setter
    def is_retry_with_the_same_operation_id(self, value: Optional[bool]) -> None:
        self.__is_retry_with_the_same_operation_id = value

    @property
    def online_pin_data(self) -> Optional[OnlinePinData]:
        """
        | In case of online PIN verification, send this object with the appropriate values.
        |
        | Depending on the acquirer, different PIN encryption types are supported. Please check with your Worldline contact which encryption type is supported for your account.

        Type: :class:`worldline.acquiring.sdk.v1.domain.online_pin_data.OnlinePinData`
        """
        return self.__online_pin_data

    @online_pin_data.setter
    def online_pin_data(self, value: Optional[OnlinePinData]) -> None:
        self.__online_pin_data = value

    @property
    def track2_data(self) -> Optional[str]:
        """
        | Track 2 data from the card
        | It is needed when cardEntryMode is MAGNETIC_STRIPE.

        Type: str
        """
        return self.__track2_data

    @track2_data.setter
    def track2_data(self, value: Optional[str]) -> None:
        self.__track2_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(PointOfSaleData, self).to_dictionary()
        if self.emv_data is not None:
            dictionary['emvData'] = []
            for element in self.emv_data:
                if element is not None:
                    dictionary['emvData'].append(element.to_dictionary())
        if self.is_response_to_pin_request is not None:
            dictionary['isResponseToPinRequest'] = self.is_response_to_pin_request
        if self.is_retry_with_the_same_operation_id is not None:
            dictionary['isRetryWithTheSameOperationId'] = self.is_retry_with_the_same_operation_id
        if self.online_pin_data is not None:
            dictionary['onlinePinData'] = self.online_pin_data.to_dictionary()
        if self.track2_data is not None:
            dictionary['track2Data'] = self.track2_data
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PointOfSaleData':
        super(PointOfSaleData, self).from_dictionary(dictionary)
        if 'emvData' in dictionary:
            if not isinstance(dictionary['emvData'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['emvData']))
            self.emv_data = []
            for element in dictionary['emvData']:
                value = EmvDataItem()
                self.emv_data.append(value.from_dictionary(element))
        if 'isResponseToPinRequest' in dictionary:
            self.is_response_to_pin_request = dictionary['isResponseToPinRequest']
        if 'isRetryWithTheSameOperationId' in dictionary:
            self.is_retry_with_the_same_operation_id = dictionary['isRetryWithTheSameOperationId']
        if 'onlinePinData' in dictionary:
            if not isinstance(dictionary['onlinePinData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['onlinePinData']))
            value = OnlinePinData()
            self.online_pin_data = value.from_dictionary(dictionary['onlinePinData'])
        if 'track2Data' in dictionary:
            self.track2_data = dictionary['track2Data']
        return self
