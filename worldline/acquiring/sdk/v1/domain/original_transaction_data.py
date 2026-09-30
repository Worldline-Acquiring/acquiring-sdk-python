# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_data import AmountData
from .payment_method_data import PaymentMethodData
from .transaction_references_dispute import TransactionReferencesDispute

from worldline.acquiring.sdk.domain.data_object import DataObject


class OriginalTransactionData(DataObject):

    __cardholder_verification_method: Optional[str] = None
    __local_transaction_date_time: Optional[str] = None
    __payment_category: Optional[str] = None
    __payment_method_data: Optional[PaymentMethodData] = None
    __point_of_sale_entry_mode: Optional[str] = None
    __scheme_processed_date_time: Optional[str] = None
    __settlement_amount: Optional[AmountData] = None
    __transaction_amount: Optional[AmountData] = None
    __transaction_references: Optional[TransactionReferencesDispute] = None

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
    def local_transaction_date_time(self) -> Optional[str]:
        """
        | The local date and time of the original transaction capture that resulted in the dispute, in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__local_transaction_date_time

    @local_transaction_date_time.setter
    def local_transaction_date_time(self, value: Optional[str]) -> None:
        self.__local_transaction_date_time = value

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
    def payment_method_data(self) -> Optional[PaymentMethodData]:
        """
        | The payment method used in the original transaction that led to the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.payment_method_data.PaymentMethodData`
        """
        return self.__payment_method_data

    @payment_method_data.setter
    def payment_method_data(self, value: Optional[PaymentMethodData]) -> None:
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
    def scheme_processed_date_time(self) -> Optional[str]:
        """
        | The date and time when the dispute was processed by the card scheme, in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__scheme_processed_date_time

    @scheme_processed_date_time.setter
    def scheme_processed_date_time(self, value: Optional[str]) -> None:
        self.__scheme_processed_date_time = value

    @property
    def settlement_amount(self) -> Optional[AmountData]:
        """
        | Amount for the operation.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value: Optional[AmountData]) -> None:
        self.__settlement_amount = value

    @property
    def transaction_amount(self) -> Optional[AmountData]:
        """
        | Amount for the operation.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value: Optional[AmountData]) -> None:
        self.__transaction_amount = value

    @property
    def transaction_references(self) -> Optional[TransactionReferencesDispute]:
        """
        | A full set of references related to the original transaction that led to the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.transaction_references_dispute.TransactionReferencesDispute`
        """
        return self.__transaction_references

    @transaction_references.setter
    def transaction_references(self, value: Optional[TransactionReferencesDispute]) -> None:
        self.__transaction_references = value

    def to_dictionary(self) -> dict:
        dictionary = super(OriginalTransactionData, self).to_dictionary()
        if self.cardholder_verification_method is not None:
            dictionary['cardholderVerificationMethod'] = self.cardholder_verification_method
        if self.local_transaction_date_time is not None:
            dictionary['localTransactionDateTime'] = self.local_transaction_date_time
        if self.payment_category is not None:
            dictionary['paymentCategory'] = self.payment_category
        if self.payment_method_data is not None:
            dictionary['paymentMethodData'] = self.payment_method_data.to_dictionary()
        if self.point_of_sale_entry_mode is not None:
            dictionary['pointOfSaleEntryMode'] = self.point_of_sale_entry_mode
        if self.scheme_processed_date_time is not None:
            dictionary['schemeProcessedDateTime'] = self.scheme_processed_date_time
        if self.settlement_amount is not None:
            dictionary['settlementAmount'] = self.settlement_amount.to_dictionary()
        if self.transaction_amount is not None:
            dictionary['transactionAmount'] = self.transaction_amount.to_dictionary()
        if self.transaction_references is not None:
            dictionary['transactionReferences'] = self.transaction_references.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OriginalTransactionData':
        super(OriginalTransactionData, self).from_dictionary(dictionary)
        if 'cardholderVerificationMethod' in dictionary:
            self.cardholder_verification_method = dictionary['cardholderVerificationMethod']
        if 'localTransactionDateTime' in dictionary:
            self.local_transaction_date_time = dictionary['localTransactionDateTime']
        if 'paymentCategory' in dictionary:
            self.payment_category = dictionary['paymentCategory']
        if 'paymentMethodData' in dictionary:
            if not isinstance(dictionary['paymentMethodData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentMethodData']))
            value = PaymentMethodData()
            self.payment_method_data = value.from_dictionary(dictionary['paymentMethodData'])
        if 'pointOfSaleEntryMode' in dictionary:
            self.point_of_sale_entry_mode = dictionary['pointOfSaleEntryMode']
        if 'schemeProcessedDateTime' in dictionary:
            self.scheme_processed_date_time = dictionary['schemeProcessedDateTime']
        if 'settlementAmount' in dictionary:
            if not isinstance(dictionary['settlementAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['settlementAmount']))
            value = AmountData()
            self.settlement_amount = value.from_dictionary(dictionary['settlementAmount'])
        if 'transactionAmount' in dictionary:
            if not isinstance(dictionary['transactionAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['transactionAmount']))
            value = AmountData()
            self.transaction_amount = value.from_dictionary(dictionary['transactionAmount'])
        if 'transactionReferences' in dictionary:
            if not isinstance(dictionary['transactionReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['transactionReferences']))
            value = TransactionReferencesDispute()
            self.transaction_references = value.from_dictionary(dictionary['transactionReferences'])
        return self
