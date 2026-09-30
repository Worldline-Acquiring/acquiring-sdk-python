# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .payment_method_data_base import PaymentMethodDataBase


class PaymentMethodData(PaymentMethodDataBase):

    __issuing_country_code: Optional[str] = None

    @property
    def issuing_country_code(self) -> Optional[str]:
        """
        | Address country code, ISO 3166 international standard

        Type: str
        """
        return self.__issuing_country_code

    @issuing_country_code.setter
    def issuing_country_code(self, value: Optional[str]) -> None:
        self.__issuing_country_code = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentMethodData, self).to_dictionary()
        if self.issuing_country_code is not None:
            dictionary['issuingCountryCode'] = self.issuing_country_code
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentMethodData':
        super(PaymentMethodData, self).from_dictionary(dictionary)
        if 'issuingCountryCode' in dictionary:
            self.issuing_country_code = dictionary['issuingCountryCode']
        return self
