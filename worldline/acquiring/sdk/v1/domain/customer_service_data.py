# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class CustomerServiceData(DataObject):

    __customer_service_email: Optional[str] = None
    __customer_service_phone_number: Optional[str] = None
    __customer_service_url: Optional[str] = None

    @property
    def customer_service_email(self) -> Optional[str]:
        """
        | Submerchant's customer service email address. Applicable only for Amex transactions but this field could be set for other scheme transactions too. Mandatory for all card not present transactions processed through Bambora.

        Type: str
        """
        return self.__customer_service_email

    @customer_service_email.setter
    def customer_service_email(self, value: Optional[str]) -> None:
        self.__customer_service_email = value

    @property
    def customer_service_phone_number(self) -> Optional[str]:
        """
        | Submerchant's customer service phone number that can be used for transaction inquiries. Applicable for MasterCard transactions but this field could be set for other scheme transactions too. Optional for all card not present transactions. Either ``CustomerServiceUrl`` or ``CustomerServicePhoneNumber`` is mandatory for card present transactions.

        Type: str
        """
        return self.__customer_service_phone_number

    @customer_service_phone_number.setter
    def customer_service_phone_number(self, value: Optional[str]) -> None:
        self.__customer_service_phone_number = value

    @property
    def customer_service_url(self) -> Optional[str]:
        """
        | Submerchant's customer service portal URL Applicable for MasterCard transactions but this field could be set for other scheme transactions too. Mandatory for all card not present transactions processed through Bambora. Either ``CustomerServiceUrl`` or ``CustomerServicePhoneNumber`` is mandatory for card present transactions.

        Type: str
        """
        return self.__customer_service_url

    @customer_service_url.setter
    def customer_service_url(self, value: Optional[str]) -> None:
        self.__customer_service_url = value

    def to_dictionary(self) -> dict:
        dictionary = super(CustomerServiceData, self).to_dictionary()
        if self.customer_service_email is not None:
            dictionary['customerServiceEmail'] = self.customer_service_email
        if self.customer_service_phone_number is not None:
            dictionary['customerServicePhoneNumber'] = self.customer_service_phone_number
        if self.customer_service_url is not None:
            dictionary['customerServiceUrl'] = self.customer_service_url
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CustomerServiceData':
        super(CustomerServiceData, self).from_dictionary(dictionary)
        if 'customerServiceEmail' in dictionary:
            self.customer_service_email = dictionary['customerServiceEmail']
        if 'customerServicePhoneNumber' in dictionary:
            self.customer_service_phone_number = dictionary['customerServicePhoneNumber']
        if 'customerServiceUrl' in dictionary:
            self.customer_service_url = dictionary['customerServiceUrl']
        return self
