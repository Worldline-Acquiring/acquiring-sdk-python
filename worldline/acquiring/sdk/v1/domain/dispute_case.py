# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .amount_data import AmountData
from .dispute_date_time_data import DisputeDateTimeData
from .dispute_merchant_data import DisputeMerchantData
from .dispute_references import DisputeReferences
from .original_transaction_data import OriginalTransactionData
from .signed_amount_data import SignedAmountData

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeCase(DataObject):

    __dispute_date_time_data: Optional[DisputeDateTimeData] = None
    __dispute_id: Optional[str] = None
    __dispute_references: Optional[DisputeReferences] = None
    __dispute_stage: Optional[str] = None
    __dispute_status: Optional[str] = None
    __dispute_status_category: Optional[str] = None
    __is_open: Optional[bool] = None
    __merchant_balance_amount: Optional[SignedAmountData] = None
    __merchant_data: Optional[DisputeMerchantData] = None
    __original_dispute_amount: Optional[AmountData] = None
    __original_transaction_data: Optional[OriginalTransactionData] = None
    __scheme_reason: Optional[str] = None
    __scheme_reason_description: Optional[str] = None
    __unified_category: Optional[str] = None
    __unified_reason: Optional[str] = None

    @property
    def dispute_date_time_data(self) -> Optional[DisputeDateTimeData]:
        """
        | A set of date time fields related to the dispute case. Depending on the ``disputeStatus`` and ``disputeStage`` of the dispute, different date time fields are relevant. For example, when the ``disputeStatus`` is "EVIDENCE_REQUESTED", the ``responseDueDate`` field indicates the deadline to respond to the dispute.
        |
        | The ``closedDateTime`` field represents the date and time when the dispute was closed. This field is only returned for closed disputes. Disputes that are open too long are automatically closed.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_date_time_data.DisputeDateTimeData`
        """
        return self.__dispute_date_time_data

    @dispute_date_time_data.setter
    def dispute_date_time_data(self, value: Optional[DisputeDateTimeData]) -> None:
        self.__dispute_date_time_data = value

    @property
    def dispute_id(self) -> Optional[str]:
        """
        | The unique identifier for a dispute.

        Type: str
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value: Optional[str]) -> None:
        self.__dispute_id = value

    @property
    def dispute_references(self) -> Optional[DisputeReferences]:
        """
        | A set of references related to the dispute case.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_references.DisputeReferences`
        """
        return self.__dispute_references

    @dispute_references.setter
    def dispute_references(self, value: Optional[DisputeReferences]) -> None:
        self.__dispute_references = value

    @property
    def dispute_stage(self) -> Optional[str]:
        """
        | The current stage in the lifecycle of the dispute.
        |
        | Possible values are:
        
        * CREATED (The dispute case includes no dispute relevant information)
        * FRAUD (The dispute case is opened with a fraud report (Issuer cases only))
        * INQUIRY (Pre-dispute phase)
        * DISPUTE (The dispute case reached the dispute stage, which includes dispute and representment handling)
        * PRE_ARBITRATION (The dispute case is in the first stage of the case filing process, before escalation to arbitration)
        * ARBITRATION (The dispute case filing process escalated to the arbitration phase)
        * PRE_COMPLIANCE (The dispute case is in the first stage of the case filing process, before escalation to compliance)
        * COMPLIANCE (The dispute case filing process escalated to the compliance phase)

        Type: str
        """
        return self.__dispute_stage

    @dispute_stage.setter
    def dispute_stage(self, value: Optional[str]) -> None:
        self.__dispute_stage = value

    @property
    def dispute_status(self) -> Optional[str]:
        """
        | The current status of the dispute.
        |
        | Possible values are:
        
        * For ``IN_PROGRESS`` dispute status category:
        
          * REVIEW_BY_ACQUIRER (Next action is on Acquirer side)
          * REVIEW_BY_ISSUER (Next action is on Issuer side)
          * REVIEW_BY_SCHEME (Next action is on Scheme side)
        * For ``NEEDS_RESPONSE`` dispute status category:
        
          * EVIDENCE_REQUESTED (Acquirer request evidence from merchant)
        * For ``WON`` dispute status category:
        
          * ISSUER_WITHDRAWN (Issuer withdraw the dispute and accept liability)
          * SUCCESSFUL_DEFENSE (Acquirer dispute defense was successful)
          * SCHEME_RULING (Dispute is escalated and scheme ruled in favor of Merchant)
        * For ``LOST`` dispute status category:
        
          * UNSUCCESSFUL_DEFENSE (Acquirer dispute defense was not successful)
          * UNANSWERED_EXPIRED (Dispute respond time expired, no further defense is possible)
          * ACCEPTED (Acquirer accepted liability)
          * SCHEME_RULING (Dispute is escalated and scheme ruled in favor of Issuer)
        * For ``CANCELLED`` dispute status category:
        
          * DISPUTE_CANCELLED (Issuer withdrew the dispute)

        Type: str
        """
        return self.__dispute_status

    @dispute_status.setter
    def dispute_status(self, value: Optional[str]) -> None:
        self.__dispute_status = value

    @property
    def dispute_status_category(self) -> Optional[str]:
        """
        | The category of the current status of the dispute.
        |
        | Possible values are:
        
        * IN_PROGRESS (Dispute process is ongoing and has no final decision. The merchant currently waits for further status updates.)
        * NEEDS_RESPONSE (The merchant is contacted to provide supporting evidence documents before a deadline)
        * WON (Dispute case has been won)
        * LOST (Dispute case has been lost)
        * CANCELLED (Dispute has been withdrawn)

        Type: str
        """
        return self.__dispute_status_category

    @dispute_status_category.setter
    def dispute_status_category(self, value: Optional[str]) -> None:
        self.__dispute_status_category = value

    @property
    def is_open(self) -> Optional[bool]:
        """
        | Indicates whether the dispute is open or closed. An open dispute is a dispute that's still in the process of being resolved, while a closed dispute is a dispute that has been resolved.

        Type: bool
        """
        return self.__is_open

    @is_open.setter
    def is_open(self, value: Optional[bool]) -> None:
        self.__is_open = value

    @property
    def merchant_balance_amount(self) -> Optional[SignedAmountData]:
        """
        | Amount with an indicator whether it's a debit or credit amount.

        Type: :class:`worldline.acquiring.sdk.v1.domain.signed_amount_data.SignedAmountData`
        """
        return self.__merchant_balance_amount

    @merchant_balance_amount.setter
    def merchant_balance_amount(self, value: Optional[SignedAmountData]) -> None:
        self.__merchant_balance_amount = value

    @property
    def merchant_data(self) -> Optional[DisputeMerchantData]:
        """
        | Data related to the merchant involved in the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_merchant_data.DisputeMerchantData`
        """
        return self.__merchant_data

    @merchant_data.setter
    def merchant_data(self, value: Optional[DisputeMerchantData]) -> None:
        self.__merchant_data = value

    @property
    def original_dispute_amount(self) -> Optional[AmountData]:
        """
        | Amount for the operation.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__original_dispute_amount

    @original_dispute_amount.setter
    def original_dispute_amount(self, value: Optional[AmountData]) -> None:
        self.__original_dispute_amount = value

    @property
    def original_transaction_data(self) -> Optional[OriginalTransactionData]:
        """
        | Data related to the original transaction that led to the dispute.

        Type: :class:`worldline.acquiring.sdk.v1.domain.original_transaction_data.OriginalTransactionData`
        """
        return self.__original_transaction_data

    @original_transaction_data.setter
    def original_transaction_data(self, value: Optional[OriginalTransactionData]) -> None:
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
        dictionary = super(DisputeCase, self).to_dictionary()
        if self.dispute_date_time_data is not None:
            dictionary['disputeDateTimeData'] = self.dispute_date_time_data.to_dictionary()
        if self.dispute_id is not None:
            dictionary['disputeId'] = self.dispute_id
        if self.dispute_references is not None:
            dictionary['disputeReferences'] = self.dispute_references.to_dictionary()
        if self.dispute_stage is not None:
            dictionary['disputeStage'] = self.dispute_stage
        if self.dispute_status is not None:
            dictionary['disputeStatus'] = self.dispute_status
        if self.dispute_status_category is not None:
            dictionary['disputeStatusCategory'] = self.dispute_status_category
        if self.is_open is not None:
            dictionary['isOpen'] = self.is_open
        if self.merchant_balance_amount is not None:
            dictionary['merchantBalanceAmount'] = self.merchant_balance_amount.to_dictionary()
        if self.merchant_data is not None:
            dictionary['merchantData'] = self.merchant_data.to_dictionary()
        if self.original_dispute_amount is not None:
            dictionary['originalDisputeAmount'] = self.original_dispute_amount.to_dictionary()
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

    def from_dictionary(self, dictionary: dict) -> 'DisputeCase':
        super(DisputeCase, self).from_dictionary(dictionary)
        if 'disputeDateTimeData' in dictionary:
            if not isinstance(dictionary['disputeDateTimeData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['disputeDateTimeData']))
            value = DisputeDateTimeData()
            self.dispute_date_time_data = value.from_dictionary(dictionary['disputeDateTimeData'])
        if 'disputeId' in dictionary:
            self.dispute_id = dictionary['disputeId']
        if 'disputeReferences' in dictionary:
            if not isinstance(dictionary['disputeReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['disputeReferences']))
            value = DisputeReferences()
            self.dispute_references = value.from_dictionary(dictionary['disputeReferences'])
        if 'disputeStage' in dictionary:
            self.dispute_stage = dictionary['disputeStage']
        if 'disputeStatus' in dictionary:
            self.dispute_status = dictionary['disputeStatus']
        if 'disputeStatusCategory' in dictionary:
            self.dispute_status_category = dictionary['disputeStatusCategory']
        if 'isOpen' in dictionary:
            self.is_open = dictionary['isOpen']
        if 'merchantBalanceAmount' in dictionary:
            if not isinstance(dictionary['merchantBalanceAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantBalanceAmount']))
            value = SignedAmountData()
            self.merchant_balance_amount = value.from_dictionary(dictionary['merchantBalanceAmount'])
        if 'merchantData' in dictionary:
            if not isinstance(dictionary['merchantData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantData']))
            value = DisputeMerchantData()
            self.merchant_data = value.from_dictionary(dictionary['merchantData'])
        if 'originalDisputeAmount' in dictionary:
            if not isinstance(dictionary['originalDisputeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['originalDisputeAmount']))
            value = AmountData()
            self.original_dispute_amount = value.from_dictionary(dictionary['originalDisputeAmount'])
        if 'originalTransactionData' in dictionary:
            if not isinstance(dictionary['originalTransactionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['originalTransactionData']))
            value = OriginalTransactionData()
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
