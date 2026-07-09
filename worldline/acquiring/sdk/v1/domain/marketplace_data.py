# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class MarketplaceData(DataObject):

    __retailer_country_code: Optional[str] = None
    __retailer_name: Optional[str] = None

    @property
    def retailer_country_code(self) -> Optional[str]:
        """
        | Address country code, ISO 3166 international standard

        Type: str
        """
        return self.__retailer_country_code

    @retailer_country_code.setter
    def retailer_country_code(self, value: Optional[str]) -> None:
        self.__retailer_country_code = value

    @property
    def retailer_name(self) -> Optional[str]:
        """
        | Name of the retailer in the marketplace

        Type: str
        """
        return self.__retailer_name

    @retailer_name.setter
    def retailer_name(self, value: Optional[str]) -> None:
        self.__retailer_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(MarketplaceData, self).to_dictionary()
        if self.retailer_country_code is not None:
            dictionary['retailerCountryCode'] = self.retailer_country_code
        if self.retailer_name is not None:
            dictionary['retailerName'] = self.retailer_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MarketplaceData':
        super(MarketplaceData, self).from_dictionary(dictionary)
        if 'retailerCountryCode' in dictionary:
            self.retailer_country_code = dictionary['retailerCountryCode']
        if 'retailerName' in dictionary:
            self.retailer_name = dictionary['retailerName']
        return self
