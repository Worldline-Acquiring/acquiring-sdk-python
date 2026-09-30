# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .customer_service_data import CustomerServiceData

from worldline.acquiring.sdk.domain.data_object import DataObject


class MerchantData(DataObject):

    __address: Optional[str] = None
    __city: Optional[str] = None
    __country_code: Optional[str] = None
    __customer_service_data: Optional[CustomerServiceData] = None
    __merchant_category_code: Optional[int] = None
    __name: Optional[str] = None
    __payment_facilitator_id: Optional[str] = None
    __postal_code: Optional[str] = None
    __state_code: Optional[str] = None
    __sub_merchant_id: Optional[str] = None
    __tax_id: Optional[str] = None

    @property
    def address(self) -> Optional[str]:
        """
        | Street address

        Type: str
        """
        return self.__address

    @address.setter
    def address(self, value: Optional[str]) -> None:
        self.__address = value

    @property
    def city(self) -> Optional[str]:
        """
        | Address city

        Type: str
        """
        return self.__city

    @city.setter
    def city(self, value: Optional[str]) -> None:
        self.__city = value

    @property
    def country_code(self) -> Optional[str]:
        """
        | Address country code, ISO 3166 international standard

        Type: str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value: Optional[str]) -> None:
        self.__country_code = value

    @property
    def customer_service_data(self) -> Optional[CustomerServiceData]:
        """
        | Customer Service Data

        Type: :class:`worldline.acquiring.sdk.v1.domain.customer_service_data.CustomerServiceData`
        """
        return self.__customer_service_data

    @customer_service_data.setter
    def customer_service_data(self, value: Optional[CustomerServiceData]) -> None:
        self.__customer_service_data = value

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
    def name(self) -> Optional[str]:
        """
        | Merchant name

        Type: str
        """
        return self.__name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self.__name = value

    @property
    def payment_facilitator_id(self) -> Optional[str]:
        """
        | Payment Facilitator identifier as assigned by Worldline

        Type: str
        """
        return self.__payment_facilitator_id

    @payment_facilitator_id.setter
    def payment_facilitator_id(self, value: Optional[str]) -> None:
        self.__payment_facilitator_id = value

    @property
    def postal_code(self) -> Optional[str]:
        """
        | Address postal code

        Type: str
        """
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, value: Optional[str]) -> None:
        self.__postal_code = value

    @property
    def state_code(self) -> Optional[str]:
        """
        | Address state code, only supplied if country is US or CA

        Type: str
        """
        return self.__state_code

    @state_code.setter
    def state_code(self, value: Optional[str]) -> None:
        self.__state_code = value

    @property
    def sub_merchant_id(self) -> Optional[str]:
        """
        | Sub-merchant identifier in the context of a Payment Facilitator.

        Type: str
        """
        return self.__sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value: Optional[str]) -> None:
        self.__sub_merchant_id = value

    @property
    def tax_id(self) -> Optional[str]:
        """
        | Applicable for Payment Facilitator submerchants located in France, Belgium or Luxembourg & having a valid national SIRET/Tax ID when using Bambora as the acquirer.

        Type: str
        """
        return self.__tax_id

    @tax_id.setter
    def tax_id(self, value: Optional[str]) -> None:
        self.__tax_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(MerchantData, self).to_dictionary()
        if self.address is not None:
            dictionary['address'] = self.address
        if self.city is not None:
            dictionary['city'] = self.city
        if self.country_code is not None:
            dictionary['countryCode'] = self.country_code
        if self.customer_service_data is not None:
            dictionary['customerServiceData'] = self.customer_service_data.to_dictionary()
        if self.merchant_category_code is not None:
            dictionary['merchantCategoryCode'] = self.merchant_category_code
        if self.name is not None:
            dictionary['name'] = self.name
        if self.payment_facilitator_id is not None:
            dictionary['paymentFacilitatorId'] = self.payment_facilitator_id
        if self.postal_code is not None:
            dictionary['postalCode'] = self.postal_code
        if self.state_code is not None:
            dictionary['stateCode'] = self.state_code
        if self.sub_merchant_id is not None:
            dictionary['subMerchantId'] = self.sub_merchant_id
        if self.tax_id is not None:
            dictionary['taxId'] = self.tax_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'MerchantData':
        super(MerchantData, self).from_dictionary(dictionary)
        if 'address' in dictionary:
            self.address = dictionary['address']
        if 'city' in dictionary:
            self.city = dictionary['city']
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'customerServiceData' in dictionary:
            if not isinstance(dictionary['customerServiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customerServiceData']))
            value = CustomerServiceData()
            self.customer_service_data = value.from_dictionary(dictionary['customerServiceData'])
        if 'merchantCategoryCode' in dictionary:
            self.merchant_category_code = dictionary['merchantCategoryCode']
        if 'name' in dictionary:
            self.name = dictionary['name']
        if 'paymentFacilitatorId' in dictionary:
            self.payment_facilitator_id = dictionary['paymentFacilitatorId']
        if 'postalCode' in dictionary:
            self.postal_code = dictionary['postalCode']
        if 'stateCode' in dictionary:
            self.state_code = dictionary['stateCode']
        if 'subMerchantId' in dictionary:
            self.sub_merchant_id = dictionary['subMerchantId']
        if 'taxId' in dictionary:
            self.tax_id = dictionary['taxId']
        return self
