# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import List, Optional

from .amount_data import AmountData
from .dispute_document import DisputeDocument

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeEntry(DataObject):

    __documents: Optional[List[DisputeDocument]] = None
    __elaboration: Optional[str] = None
    __entry_category: Optional[str] = None
    __entry_date_time: Optional[str] = None
    __entry_id: Optional[str] = None
    __entry_type: Optional[str] = None
    __entry_type_description: Optional[str] = None
    __message_text: Optional[str] = None
    __questionnaire: Optional[str] = None
    __response_due_date: Optional[date] = None
    __scheme_reason: Optional[str] = None
    __scheme_reason_description: Optional[str] = None
    __settlement_amount: Optional[AmountData] = None
    __transaction_amount: Optional[AmountData] = None
    __user_id: Optional[str] = None

    @property
    def documents(self) -> Optional[List[DisputeDocument]]:
        """
        | A list of documents related to the history entry.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.dispute_document.DisputeDocument`]
        """
        return self.__documents

    @documents.setter
    def documents(self, value: Optional[List[DisputeDocument]]) -> None:
        self.__documents = value

    @property
    def elaboration(self) -> Optional[str]:
        """
        | The long message text of the dispute entry, if applicable. This is typically used for communication entries to provide the content of the message sent by the acquirer to the merchant or vice versa. This field can contain a more detailed message than the ``messageText`` property.

        Type: str
        """
        return self.__elaboration

    @elaboration.setter
    def elaboration(self, value: Optional[str]) -> None:
        self.__elaboration = value

    @property
    def entry_category(self) -> Optional[str]:
        """
        | The category of the dispute entry.
        |
        | Possible values are:
        
        * ``DISPUTE``	(Transaction which drives the scheme dispute processing flow)
        * ``COMMUNICATION``	(Conversational and informational messages which are exchanged in the communication between Acquirer and Merchant)
        * ``EVIDENCE`` (Merchant response to Acquirer Evidence Request (including liability acceptance))
        * ``POSTING`` (Notification about upcoming Merchant account adjustments, executed by the Acquirer)

        Type: str
        """
        return self.__entry_category

    @entry_category.setter
    def entry_category(self, value: Optional[str]) -> None:
        self.__entry_category = value

    @property
    def entry_date_time(self) -> Optional[str]:
        """
        | The date and time when the dispute entry was made, in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__entry_date_time

    @entry_date_time.setter
    def entry_date_time(self, value: Optional[str]) -> None:
        self.__entry_date_time = value

    @property
    def entry_id(self) -> Optional[str]:
        """
        | The unique identifier for an dispute entry.

        Type: str
        """
        return self.__entry_id

    @entry_id.setter
    def entry_id(self, value: Optional[str]) -> None:
        self.__entry_id = value

    @property
    def entry_type(self) -> Optional[str]:
        """
        | The type of the dispute entry. The values for this field depend on the value of the ``EntryCategory`` field.
        |
        | Possible values are:
        
        * For DISPUTE entry Category:
        
          * ``Iss-Dsp`` (Issuer dispute (full/partial))
          * ``Iss-DspRev`` (Issuer reversed dispute)
          * ``Iss-ArbDsp`` (Issuer Arbitration dispute (full/partial))
          * ``Iss-PArb`` (Issuer Pre-Arbitration (full/partial))
          * ``Iss-PComp`` (Issuer Pre-Compliance)
          * ``Iss-Arb`` (Issuer Arbitration)
          * 'Iss-Comp' (Issuer Compliance)
          * ``Acq-PArb`` (Acquirer Pre-Arbitration (full/partial))
          * ``Acq-PComp`` (Acquirer Pre-Compliance)
          * ``Acq-Arb`` (Acquirer Arbitration)
          * ``Acq-Comp`` (Acquirer Compliance)
          * ``Acq-DspDecline`` (Acquirer Declines Dispute (full/partial))
          * ``Acq-ArbDspDecline`` (Acquirer Declines Arbitration Dispute (full/partial))
          * ``Acq-PArbDecline`` (Acquirer Declines Pre-Arbitration (full/partial))
          * ``Acq-PCompDecline`` (Acquirer Declines Pre-Compliance (full/partial))
          * ``Iss-PArbDecline`` (Issuer Declines Pre-Arbitration (full/partial))
          * ``Iss-PCompDecline`` (Issuer Declines Pre-Compliance (full/partial))
          * ``Acq-MchLost`` (Dispute case is lost, Liability on Acquirer)
          * ``Acq-MchWon`` (Dispute case is won, Liability on Issuer)
        * For COMMUNICATION entryCategory:
        
          * ``Acq-MsgToMch`` (Acquirer sent a message to the Merchant)
          * ``Mch-MsgToAcq`` (Merchant sent a message to the Acquirer)
        * For EVIDENCE entryCategory:
        
          * ``Acq-EvidenceReq`` (Acquirer request evidence from Merchant)
          * ``Acq-EvidenceRej`` (Acquirer reject the evidence submitted by the Merchant)
          * ``Mch-Evidence`` (Merchant submitted evidence)
          * ``Mch-Accept`` (Merchant accepted liability)
        * For POSTING entryCategory:
        
          * ``Acq-CreditAdj`` (Acquirer credited the Merchant)
          * ``Acq-DebitAdj`` (Acquirer debited the Merchant)

        Type: str
        """
        return self.__entry_type

    @entry_type.setter
    def entry_type(self, value: Optional[str]) -> None:
        self.__entry_type = value

    @property
    def entry_type_description(self) -> Optional[str]:
        """
        | The human readable description of the ``EntryType`` field.

        Type: str
        """
        return self.__entry_type_description

    @entry_type_description.setter
    def entry_type_description(self, value: Optional[str]) -> None:
        self.__entry_type_description = value

    @property
    def message_text(self) -> Optional[str]:
        """
        | The message text of the dispute entry, if applicable. This is typically used for communication entries to provide the content of the message sent by the acquirer to the merchant or vice versa.

        Type: str
        """
        return self.__message_text

    @message_text.setter
    def message_text(self, value: Optional[str]) -> None:
        self.__message_text = value

    @property
    def questionnaire(self) -> Optional[str]:
        """
        | The questionnaire provided by the card scheme for the dispute, if applicable. This is typically used for communication entries to provide the content of the questionnaire sent by the acquirer to the merchant in case the card scheme requires a specific set of questions to be answered by the merchant in order to provide evidence for the dispute case.

        Type: str
        """
        return self.__questionnaire

    @questionnaire.setter
    def questionnaire(self, value: Optional[str]) -> None:
        self.__questionnaire = value

    @property
    def response_due_date(self) -> Optional[date]:
        """
        | The date when a response to the dispute is due. This field is typically relevant when the ``disputeStatus`` is "EVIDENCE_REQUESTED", to indicate the deadline to respond to the dispute.

        Type: date
        """
        return self.__response_due_date

    @response_due_date.setter
    def response_due_date(self, value: Optional[date]) -> None:
        self.__response_due_date = value

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
    def user_id(self) -> Optional[str]:
        """
        | The unique identifier of the user that triggered the dispute entry, if applicable.

        Type: str
        """
        return self.__user_id

    @user_id.setter
    def user_id(self, value: Optional[str]) -> None:
        self.__user_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeEntry, self).to_dictionary()
        if self.documents is not None:
            dictionary['documents'] = []
            for element in self.documents:
                if element is not None:
                    dictionary['documents'].append(element.to_dictionary())
        if self.elaboration is not None:
            dictionary['elaboration'] = self.elaboration
        if self.entry_category is not None:
            dictionary['entryCategory'] = self.entry_category
        if self.entry_date_time is not None:
            dictionary['entryDateTime'] = self.entry_date_time
        if self.entry_id is not None:
            dictionary['entryId'] = self.entry_id
        if self.entry_type is not None:
            dictionary['entryType'] = self.entry_type
        if self.entry_type_description is not None:
            dictionary['entryTypeDescription'] = self.entry_type_description
        if self.message_text is not None:
            dictionary['messageText'] = self.message_text
        if self.questionnaire is not None:
            dictionary['questionnaire'] = self.questionnaire
        if self.response_due_date is not None:
            dictionary['responseDueDate'] = DataObject.format_date(self.response_due_date)
        if self.scheme_reason is not None:
            dictionary['schemeReason'] = self.scheme_reason
        if self.scheme_reason_description is not None:
            dictionary['schemeReasonDescription'] = self.scheme_reason_description
        if self.settlement_amount is not None:
            dictionary['settlementAmount'] = self.settlement_amount.to_dictionary()
        if self.transaction_amount is not None:
            dictionary['transactionAmount'] = self.transaction_amount.to_dictionary()
        if self.user_id is not None:
            dictionary['userId'] = self.user_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeEntry':
        super(DisputeEntry, self).from_dictionary(dictionary)
        if 'documents' in dictionary:
            if not isinstance(dictionary['documents'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['documents']))
            self.documents = []
            for element in dictionary['documents']:
                value = DisputeDocument()
                self.documents.append(value.from_dictionary(element))
        if 'elaboration' in dictionary:
            self.elaboration = dictionary['elaboration']
        if 'entryCategory' in dictionary:
            self.entry_category = dictionary['entryCategory']
        if 'entryDateTime' in dictionary:
            self.entry_date_time = dictionary['entryDateTime']
        if 'entryId' in dictionary:
            self.entry_id = dictionary['entryId']
        if 'entryType' in dictionary:
            self.entry_type = dictionary['entryType']
        if 'entryTypeDescription' in dictionary:
            self.entry_type_description = dictionary['entryTypeDescription']
        if 'messageText' in dictionary:
            self.message_text = dictionary['messageText']
        if 'questionnaire' in dictionary:
            self.questionnaire = dictionary['questionnaire']
        if 'responseDueDate' in dictionary:
            self.response_due_date = DataObject.parse_date(dictionary['responseDueDate'])
        if 'schemeReason' in dictionary:
            self.scheme_reason = dictionary['schemeReason']
        if 'schemeReasonDescription' in dictionary:
            self.scheme_reason_description = dictionary['schemeReasonDescription']
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
        if 'userId' in dictionary:
            self.user_id = dictionary['userId']
        return self
