# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .dispute_merchant_data_base import DisputeMerchantDataBase
from .original_transaction_summary_data import OriginalTransactionSummaryData

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeSummary(DataObject):

    __acquirer_dispute_reference: Optional[str] = None
    __merchant_data: Optional[DisputeMerchantDataBase] = None
    __original_transaction_data: Optional[OriginalTransactionSummaryData] = None
    __scheme_reason: Optional[str] = None
    __scheme_reason_description: Optional[str] = None
    __unified_category: Optional[str] = None
    __unified_reason: Optional[str] = None

    @property
    def acquirer_dispute_reference(self) -> Optional[str]:
        """
        | The reference provided by the acquirer for the dispute.

        Type: str
        """
        return self.__acquirer_dispute_reference

    @acquirer_dispute_reference.setter
    def acquirer_dispute_reference(self, value: Optional[str]) -> None:
        self.__acquirer_dispute_reference = value

    @property
    def merchant_data(self) -> Optional[DisputeMerchantDataBase]:
        """
        | Summary data related to the merchant involved in the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_merchant_data_base.DisputeMerchantDataBase`
        """
        return self.__merchant_data

    @merchant_data.setter
    def merchant_data(self, value: Optional[DisputeMerchantDataBase]) -> None:
        self.__merchant_data = value

    @property
    def original_transaction_data(self) -> Optional[OriginalTransactionSummaryData]:
        """
        | Data related to the original transaction that led to the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.original_transaction_summary_data.OriginalTransactionSummaryData`
        """
        return self.__original_transaction_data

    @original_transaction_data.setter
    def original_transaction_data(self, value: Optional[OriginalTransactionSummaryData]) -> None:
        self.__original_transaction_data = value

    @property
    def scheme_reason(self) -> Optional[str]:
        """
        | The reason provided by the card scheme for the dispute.

        Type: str
        """
        return self.__scheme_reason

    @scheme_reason.setter
    def scheme_reason(self, value: Optional[str]) -> None:
        self.__scheme_reason = value

    @property
    def scheme_reason_description(self) -> Optional[str]:
        """
        | The human readable description of the reason provided by the card scheme for the dispute.

        Type: str
        """
        return self.__scheme_reason_description

    @scheme_reason_description.setter
    def scheme_reason_description(self, value: Optional[str]) -> None:
        self.__scheme_reason_description = value

    @property
    def unified_category(self) -> Optional[str]:
        """
        | The unified category of the dispute, used for categorization and reporting purposes. Only present if a dispute was received.
        |
        | Possible values are:
        
        * AUTHORIZATION_RELATED (authorization related disputes)
        * FRAUD_RELATED (fraud related disputes)
        * CONSUMER_DISPUTE (consumer initiated disputes)
        * PROCESSING_ERROR (error during the payment processing leads to a dispute)
        * OTHER (collection of diverse dispute reasons)

        Type: str
        """
        return self.__unified_category

    @unified_category.setter
    def unified_category(self, value: Optional[str]) -> None:
        self.__unified_category = value

    @property
    def unified_reason(self) -> Optional[str]:
        """
        | The unified reason for the dispute, used for categorization and reporting purposes. Only present if a dispute was received.
        |
        | Possible values are:
        
        * FRAUDULENT_CARD_USAGE (Fraudulent use of card)
        * UNAUTHORIZED_TRANSACTION (No valid Issuer authorization)
        * GENERAL_PAYMENT_ERROR (General payment error)
        * INVALID_TRANSACTION_TYPE (Invalid transaction type)
        * INVALID_CURRENCY (Invalid currency)
        * INVALID_CARD_NUMBER (Invalid card number)
        * INVALID_AMOUNT (Invalid amount)
        * DUPLICATE_CHARGE_OR_PAID_BY_OTHER_MEANS (Duplicate charge or paid by other means)
        * GENERAL_CUSTOMER_DISPUTE (General customer dispute)
        * GOODS_OR_SERVICES_NOT_RECEIVED (Goods or services not received)
        * CANCELLED_SUBSCRIPTION (Cancelled subscription)
        * GOODS_OR_SERVICES_NOT_MATCHING_ORDER (Goods or services not matching order)
        * COUNTERFEIT_MERCHANDISE (Counterfeit merchandise)
        * DUE_REFUND_NOT_RECEIVED (Due refund not received)
        * CHARGE_NOT_ACCEPTED ((Subsequent) Charge not accepted)
        * OTHER (Other)

        Type: str
        """
        return self.__unified_reason

    @unified_reason.setter
    def unified_reason(self, value: Optional[str]) -> None:
        self.__unified_reason = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeSummary, self).to_dictionary()
        if self.acquirer_dispute_reference is not None:
            dictionary['acquirerDisputeReference'] = self.acquirer_dispute_reference
        if self.merchant_data is not None:
            dictionary['merchantData'] = self.merchant_data.to_dictionary()
        if self.original_transaction_data is not None:
            dictionary['originalTransactionData'] = self.original_transaction_data.to_dictionary()
        if self.scheme_reason is not None:
            dictionary['schemeReason'] = self.scheme_reason
        if self.scheme_reason_description is not None:
            dictionary['schemeReasonDescription'] = self.scheme_reason_description
        if self.unified_category is not None:
            dictionary['unifiedCategory'] = self.unified_category
        if self.unified_reason is not None:
            dictionary['unifiedReason'] = self.unified_reason
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeSummary':
        super(DisputeSummary, self).from_dictionary(dictionary)
        if 'acquirerDisputeReference' in dictionary:
            self.acquirer_dispute_reference = dictionary['acquirerDisputeReference']
        if 'merchantData' in dictionary:
            if not isinstance(dictionary['merchantData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantData']))
            value = DisputeMerchantDataBase()
            self.merchant_data = value.from_dictionary(dictionary['merchantData'])
        if 'originalTransactionData' in dictionary:
            if not isinstance(dictionary['originalTransactionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['originalTransactionData']))
            value = OriginalTransactionSummaryData()
            self.original_transaction_data = value.from_dictionary(dictionary['originalTransactionData'])
        if 'schemeReason' in dictionary:
            self.scheme_reason = dictionary['schemeReason']
        if 'schemeReasonDescription' in dictionary:
            self.scheme_reason_description = dictionary['schemeReasonDescription']
        if 'unifiedCategory' in dictionary:
            self.unified_category = dictionary['unifiedCategory']
        if 'unifiedReason' in dictionary:
            self.unified_reason = dictionary['unifiedReason']
        return self
