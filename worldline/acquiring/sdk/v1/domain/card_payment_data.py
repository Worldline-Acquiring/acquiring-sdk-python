# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .card_on_file_data import CardOnFileData
from .e_commerce_data import ECommerceData
from .network_token_data import NetworkTokenData
from .plain_card_data import PlainCardData
from .point_of_sale_data import PointOfSaleData

from worldline.acquiring.sdk.domain.data_object import DataObject


class CardPaymentData(DataObject):

    __allow_partial_approval: Optional[bool] = None
    __brand: Optional[str] = None
    __capture_immediately: Optional[bool] = None
    __card_data: Optional[PlainCardData] = None
    __card_entry_mode: Optional[str] = None
    __card_on_file_data: Optional[CardOnFileData] = None
    __cardholder_verification_method: Optional[str] = None
    __ecommerce_data: Optional[ECommerceData] = None
    __network_token_data: Optional[NetworkTokenData] = None
    __point_of_sale_data: Optional[PointOfSaleData] = None
    __wallet_id: Optional[str] = None

    @property
    def allow_partial_approval(self) -> Optional[bool]:
        """
        | Indicate wether you allow partial approval or not

        Type: bool
        """
        return self.__allow_partial_approval

    @allow_partial_approval.setter
    def allow_partial_approval(self, value: Optional[bool]) -> None:
        self.__allow_partial_approval = value

    @property
    def brand(self) -> Optional[str]:
        """
        | The card brand

        Type: str
        """
        return self.__brand

    @brand.setter
    def brand(self, value: Optional[str]) -> None:
        self.__brand = value

    @property
    def capture_immediately(self) -> Optional[bool]:
        """
        | If true the transaction will be authorized and captured immediately

        Type: bool
        """
        return self.__capture_immediately

    @capture_immediately.setter
    def capture_immediately(self, value: Optional[bool]) -> None:
        self.__capture_immediately = value

    @property
    def card_data(self) -> Optional[PlainCardData]:
        """
        | Card data in plain text

        Type: :class:`worldline.acquiring.sdk.v1.domain.plain_card_data.PlainCardData`
        """
        return self.__card_data

    @card_data.setter
    def card_data(self, value: Optional[PlainCardData]) -> None:
        self.__card_data = value

    @property
    def card_entry_mode(self) -> Optional[str]:
        """
        | Card entry mode used in the transaction, defaults to ECOMMERCE

        Type: str
        """
        return self.__card_entry_mode

    @card_entry_mode.setter
    def card_entry_mode(self, value: Optional[str]) -> None:
        self.__card_entry_mode = value

    @property
    def card_on_file_data(self) -> Optional[CardOnFileData]:
        """
        Type: :class:`worldline.acquiring.sdk.v1.domain.card_on_file_data.CardOnFileData`
        """
        return self.__card_on_file_data

    @card_on_file_data.setter
    def card_on_file_data(self, value: Optional[CardOnFileData]) -> None:
        self.__card_on_file_data = value

    @property
    def cardholder_verification_method(self) -> Optional[str]:
        """
        | Cardholder verification method used in the transaction

        Type: str
        """
        return self.__cardholder_verification_method

    @cardholder_verification_method.setter
    def cardholder_verification_method(self, value: Optional[str]) -> None:
        self.__cardholder_verification_method = value

    @property
    def ecommerce_data(self) -> Optional[ECommerceData]:
        """
        | Request data for eCommerce and MOTO transactions

        Type: :class:`worldline.acquiring.sdk.v1.domain.e_commerce_data.ECommerceData`
        """
        return self.__ecommerce_data

    @ecommerce_data.setter
    def ecommerce_data(self, value: Optional[ECommerceData]) -> None:
        self.__ecommerce_data = value

    @property
    def network_token_data(self) -> Optional[NetworkTokenData]:
        """
        Type: :class:`worldline.acquiring.sdk.v1.domain.network_token_data.NetworkTokenData`
        """
        return self.__network_token_data

    @network_token_data.setter
    def network_token_data(self, value: Optional[NetworkTokenData]) -> None:
        self.__network_token_data = value

    @property
    def point_of_sale_data(self) -> Optional[PointOfSaleData]:
        """
        | Payment terminal request data

        Type: :class:`worldline.acquiring.sdk.v1.domain.point_of_sale_data.PointOfSaleData`
        """
        return self.__point_of_sale_data

    @point_of_sale_data.setter
    def point_of_sale_data(self, value: Optional[PointOfSaleData]) -> None:
        self.__point_of_sale_data = value

    @property
    def wallet_id(self) -> Optional[str]:
        """
        | Type of wallet, values are assigned by card schemes, e.g. 101 for MasterPass in eCommerce, 102 for MasterPass NFC, 103 for Apple Pay, 216 for Google Pay and 217 for Samsung Pay

        Type: str
        """
        return self.__wallet_id

    @wallet_id.setter
    def wallet_id(self, value: Optional[str]) -> None:
        self.__wallet_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(CardPaymentData, self).to_dictionary()
        if self.allow_partial_approval is not None:
            dictionary['allowPartialApproval'] = self.allow_partial_approval
        if self.brand is not None:
            dictionary['brand'] = self.brand
        if self.capture_immediately is not None:
            dictionary['captureImmediately'] = self.capture_immediately
        if self.card_data is not None:
            dictionary['cardData'] = self.card_data.to_dictionary()
        if self.card_entry_mode is not None:
            dictionary['cardEntryMode'] = self.card_entry_mode
        if self.card_on_file_data is not None:
            dictionary['cardOnFileData'] = self.card_on_file_data.to_dictionary()
        if self.cardholder_verification_method is not None:
            dictionary['cardholderVerificationMethod'] = self.cardholder_verification_method
        if self.ecommerce_data is not None:
            dictionary['ecommerceData'] = self.ecommerce_data.to_dictionary()
        if self.network_token_data is not None:
            dictionary['networkTokenData'] = self.network_token_data.to_dictionary()
        if self.point_of_sale_data is not None:
            dictionary['pointOfSaleData'] = self.point_of_sale_data.to_dictionary()
        if self.wallet_id is not None:
            dictionary['walletId'] = self.wallet_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'CardPaymentData':
        super(CardPaymentData, self).from_dictionary(dictionary)
        if 'allowPartialApproval' in dictionary:
            self.allow_partial_approval = dictionary['allowPartialApproval']
        if 'brand' in dictionary:
            self.brand = dictionary['brand']
        if 'captureImmediately' in dictionary:
            self.capture_immediately = dictionary['captureImmediately']
        if 'cardData' in dictionary:
            if not isinstance(dictionary['cardData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardData']))
            value = PlainCardData()
            self.card_data = value.from_dictionary(dictionary['cardData'])
        if 'cardEntryMode' in dictionary:
            self.card_entry_mode = dictionary['cardEntryMode']
        if 'cardOnFileData' in dictionary:
            if not isinstance(dictionary['cardOnFileData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardOnFileData']))
            value = CardOnFileData()
            self.card_on_file_data = value.from_dictionary(dictionary['cardOnFileData'])
        if 'cardholderVerificationMethod' in dictionary:
            self.cardholder_verification_method = dictionary['cardholderVerificationMethod']
        if 'ecommerceData' in dictionary:
            if not isinstance(dictionary['ecommerceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['ecommerceData']))
            value = ECommerceData()
            self.ecommerce_data = value.from_dictionary(dictionary['ecommerceData'])
        if 'networkTokenData' in dictionary:
            if not isinstance(dictionary['networkTokenData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['networkTokenData']))
            value = NetworkTokenData()
            self.network_token_data = value.from_dictionary(dictionary['networkTokenData'])
        if 'pointOfSaleData' in dictionary:
            if not isinstance(dictionary['pointOfSaleData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pointOfSaleData']))
            value = PointOfSaleData()
            self.point_of_sale_data = value.from_dictionary(dictionary['pointOfSaleData'])
        if 'walletId' in dictionary:
            self.wallet_id = dictionary['walletId']
        return self
