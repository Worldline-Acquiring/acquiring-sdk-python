# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .payment_method_data_base import PaymentMethodDataBase
from .transaction_references_base import TransactionReferencesBase

from worldline.acquiring.sdk.domain.data_object import DataObject


class OriginalTransactionSummaryData(DataObject):

    __cardholder_verification_method: Optional[str] = None
    __payment_category: Optional[str] = None
    __payment_method_data: Optional[PaymentMethodDataBase] = None
    __point_of_sale_entry_mode: Optional[str] = None
    __transaction_references: Optional[TransactionReferencesBase] = None

    @property
    def cardholder_verification_method(self) -> Optional[str]:
        """
        | The cardholder verification method (CVM) used in the original transaction that led to the dispute.

        Type: str
        """
        return self.__cardholder_verification_method

    @cardholder_verification_method.setter
    def cardholder_verification_method(self, value: Optional[str]) -> None:
        self.__cardholder_verification_method = value

    @property
    def payment_category(self) -> Optional[str]:
        """
        | The category of the payment used in the original transaction that led to the dispute.
        |
        | Possible values are:
        
        * ``SALES`` (Different kind of payments with debits the recipient)
        * ``CREDIT_VOUCHER`` (Refund/Credit payment)
        * ``ORIGINAL_CREDIT`` (Transaction that credits the recipient in a payment transaction (money send, original credit) or cardholder funds transfer)
        * ``ATM`` (ATM Deposit)
        * ``ACCOUNT_FUNDING`` (Transaction that debits the sender in a payment transaction (money send, original credit))
        * ``CASH_ADVANCE`` (Cash advance payment)

        Type: str
        """
        return self.__payment_category

    @payment_category.setter
    def payment_category(self, value: Optional[str]) -> None:
        self.__payment_category = value

    @property
    def payment_method_data(self) -> Optional[PaymentMethodDataBase]:
        """
        | The payment method used in the original transaction that led to the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.payment_method_data_base.PaymentMethodDataBase`
        """
        return self.__payment_method_data

    @payment_method_data.setter
    def payment_method_data(self, value: Optional[PaymentMethodDataBase]) -> None:
        self.__payment_method_data = value

    @property
    def point_of_sale_entry_mode(self) -> Optional[str]:
        """
        | The point of sale (POS) entry mode used in the original transaction that led to the dispute.
        |
        | Non-exclusive list of possible values:
        
        * Unknown
        * Track1
        * Track2
        * Track3
        * Chip
        * Manual
        * Contactless-EMV
        * Contactless-Magstripe
        * Account ID
        * EMV fallback
        * Server or Wallet
        * QRC Code TAGC
        * CredentialOnFile
        * URL-intent

        Type: str
        """
        return self.__point_of_sale_entry_mode

    @point_of_sale_entry_mode.setter
    def point_of_sale_entry_mode(self, value: Optional[str]) -> None:
        self.__point_of_sale_entry_mode = value

    @property
    def transaction_references(self) -> Optional[TransactionReferencesBase]:
        """
        | A subset of references related to the original transaction that led to the dispute. The full list is returned by the `Retrieve Dispute <#operation/getDispute>`_ endpoint.

        Type: :class:`worldline.acquiring.sdk.v1.domain.transaction_references_base.TransactionReferencesBase`
        """
        return self.__transaction_references

    @transaction_references.setter
    def transaction_references(self, value: Optional[TransactionReferencesBase]) -> None:
        self.__transaction_references = value

    def to_dictionary(self) -> dict:
        dictionary = super(OriginalTransactionSummaryData, self).to_dictionary()
        if self.cardholder_verification_method is not None:
            dictionary['cardholderVerificationMethod'] = self.cardholder_verification_method
        if self.payment_category is not None:
            dictionary['paymentCategory'] = self.payment_category
        if self.payment_method_data is not None:
            dictionary['paymentMethodData'] = self.payment_method_data.to_dictionary()
        if self.point_of_sale_entry_mode is not None:
            dictionary['pointOfSaleEntryMode'] = self.point_of_sale_entry_mode
        if self.transaction_references is not None:
            dictionary['transactionReferences'] = self.transaction_references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OriginalTransactionSummaryData':
        super(OriginalTransactionSummaryData, self).from_dictionary(dictionary)
        if 'cardholderVerificationMethod' in dictionary:
            self.cardholder_verification_method = dictionary['cardholderVerificationMethod']
        if 'paymentCategory' in dictionary:
            self.payment_category = dictionary['paymentCategory']
        if 'paymentMethodData' in dictionary:
            if not isinstance(dictionary['paymentMethodData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentMethodData']))
            value = PaymentMethodDataBase()
            self.payment_method_data = value.from_dictionary(dictionary['paymentMethodData'])
        if 'pointOfSaleEntryMode' in dictionary:
            self.point_of_sale_entry_mode = dictionary['pointOfSaleEntryMode']
        if 'transactionReferences' in dictionary:
            if not isinstance(dictionary['transactionReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['transactionReferences']))
            value = TransactionReferencesBase()
            self.transaction_references = value.from_dictionary(dictionary['transactionReferences'])
        return self
