# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class PaymentMethodDataBase(DataObject):

    __masked_identifier: Optional[str] = None
    __scheme: Optional[str] = None
    __scheme_brand: Optional[str] = None

    @property
    def masked_identifier(self) -> Optional[str]:
        """
        | The masked identifier of the card used in the original transaction that led to the dispute. The masked identifier typically includes the first six and last four digits of the card number, with the middle digits replaced by asterisks or other masking characters. Different masking patterns are used for card and non-card payment methods.
        
        * Card: 717171*******1234
        * Non-Card: DE89****4567
        * Non-Card: j***@email.com

        Type: str
        """
        return self.__masked_identifier

    @masked_identifier.setter
    def masked_identifier(self, value: Optional[str]) -> None:
        self.__masked_identifier = value

    @property
    def scheme(self) -> Optional[str]:
        """
        | The card scheme used in the original transaction that led to the dispute.
        |
        | Common values:
        
        * ``MASTERCARD``	(Mastercard)
        * ``VISA``	(Visa)
        * ``JCB``	(Japan Credit Bureau)
        * ``UNION_PAY``	(UnionPay International)
        * ``DINERS``	(Diners)
        * ``EUROPEAN_PAYMENTS_INITIATIVE``	(European Payment Initiative (Wero))
        * ``CARTE_BANCAIRES``	(Cartes Bancaires)
        * ``EFTPOS``	(EFTPOS (Electronic Funds Transfer at Point of Sale))
        
        | Support for new schemes may be introduced without notice. Clients should handle unknown values gracefully.

        Type: str
        """
        return self.__scheme

    @scheme.setter
    def scheme(self, value: Optional[str]) -> None:
        self.__scheme = value

    @property
    def scheme_brand(self) -> Optional[str]:
        """
        | The card scheme brand used in the original transaction that led to the dispute.
        |
        | Possible values are:
        
        * ``MSI``	(Maestro Debit Card)
        * ``MCC``	(MasterCard Credit Card)
        * ``CIR``	(Cirrus Debit Card)
        * ``DMC``	(MasterCard Debit Card)
        * ``VISA`` (VISA Credit Card)
        * ``VPAY`` (V PAY)
        * ``PLUS`` (PLUS)
        * ``ELEC`` (Visa Electron)
        * ``JCB``	(JCB)
        * ``CUP``	(China Union Pay Credit Card)
        * ``DINER`` (DINERS credit card)
        * ``EFTPOS`` (EFTPOS, for Australia)
        * ``CB`` (Cartes Bancaires Domestic Scheme France)
        * ``WERO`` (European payment solution developed by EPI)

        Type: str
        """
        return self.__scheme_brand

    @scheme_brand.setter
    def scheme_brand(self, value: Optional[str]) -> None:
        self.__scheme_brand = value

    def to_dictionary(self) -> dict:
        dictionary = super(PaymentMethodDataBase, self).to_dictionary()
        if self.masked_identifier is not None:
            dictionary['maskedIdentifier'] = self.masked_identifier
        if self.scheme is not None:
            dictionary['scheme'] = self.scheme
        if self.scheme_brand is not None:
            dictionary['schemeBrand'] = self.scheme_brand
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PaymentMethodDataBase':
        super(PaymentMethodDataBase, self).from_dictionary(dictionary)
        if 'maskedIdentifier' in dictionary:
            self.masked_identifier = dictionary['maskedIdentifier']
        if 'scheme' in dictionary:
            self.scheme = dictionary['scheme']
        if 'schemeBrand' in dictionary:
            self.scheme_brand = dictionary['schemeBrand']
        return self
