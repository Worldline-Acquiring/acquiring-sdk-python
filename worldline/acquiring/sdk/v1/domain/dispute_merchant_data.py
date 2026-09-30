# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .dispute_merchant_data_base import DisputeMerchantDataBase


class DisputeMerchantData(DisputeMerchantDataBase):

    __merchant_category_code: Optional[int] = None
    __merchant_city: Optional[str] = None
    __merchant_country_code: Optional[str] = None
    __merchant_name: Optional[str] = None

    @property
    def merchant_category_code(self) -> Optional[int]:
        """
        | Merchant category code (MCC)

        Type: int
        """
        return self.__merchant_category_code

    @merchant_category_code.setter
    def merchant_category_code(self, value: Optional[int]) -> None:
        self.__merchant_category_code = value

    @property
    def merchant_city(self) -> Optional[str]:
        """
        | The city where the merchant is located.

        Type: str
        """
        return self.__merchant_city

    @merchant_city.setter
    def merchant_city(self, value: Optional[str]) -> None:
        self.__merchant_city = value

    @property
    def merchant_country_code(self) -> Optional[str]:
        """
        | The country code of the merchant's location in ISO 3166-1 alpha-2 format.

        Type: str
        """
        return self.__merchant_country_code

    @merchant_country_code.setter
    def merchant_country_code(self, value: Optional[str]) -> None:
        self.__merchant_country_code = value

    @property
    def merchant_name(self) -> Optional[str]:
        """
        | Merchant name

        Type: str
        """
        return self.__merchant_name

    @merchant_name.setter
    def merchant_name(self, value: Optional[str]) -> None:
        self.__merchant_name = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeMerchantData, self).to_dictionary()
        if self.merchant_category_code is not None:
            dictionary['merchantCategoryCode'] = self.merchant_category_code
        if self.merchant_city is not None:
            dictionary['merchantCity'] = self.merchant_city
        if self.merchant_country_code is not None:
            dictionary['merchantCountryCode'] = self.merchant_country_code
        if self.merchant_name is not None:
            dictionary['merchantName'] = self.merchant_name
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeMerchantData':
        super(DisputeMerchantData, self).from_dictionary(dictionary)
        if 'merchantCategoryCode' in dictionary:
            self.merchant_category_code = dictionary['merchantCategoryCode']
        if 'merchantCity' in dictionary:
            self.merchant_city = dictionary['merchantCity']
        if 'merchantCountryCode' in dictionary:
            self.merchant_country_code = dictionary['merchantCountryCode']
        if 'merchantName' in dictionary:
            self.merchant_name = dictionary['merchantName']
        return self
