# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .amount_data import AmountData
from .dispute_document_id_item import DisputeDocumentIdItem

from worldline.acquiring.sdk.domain.data_object import DataObject


class SubmitEvidenceRequest(DataObject):

    __document_ids: Optional[List[DisputeDocumentIdItem]] = None
    __elaboration: Optional[str] = None
    __include_entries: Optional[bool] = None
    __partial_amount: Optional[AmountData] = None
    __user_id: Optional[str] = None

    @property
    def document_ids(self) -> Optional[List[DisputeDocumentIdItem]]:
        """
        Type: list[:class:`worldline.acquiring.sdk.v1.domain.dispute_document_id_item.DisputeDocumentIdItem`]
        """
        return self.__document_ids

    @document_ids.setter
    def document_ids(self, value: Optional[List[DisputeDocumentIdItem]]) -> None:
        self.__document_ids = value

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
    def include_entries(self) -> Optional[bool]:
        """
        | If true, the response will include the full history of dispute entries related to the dispute. False by default.

        Type: bool
        """
        return self.__include_entries

    @include_entries.setter
    def include_entries(self, value: Optional[bool]) -> None:
        self.__include_entries = value

    @property
    def partial_amount(self) -> Optional[AmountData]:
        """
        | Optional: Challenge only a partial amount of the dispute. By providing this value, you accept automatic liability for the remaining disputed amount.
        |
        | Rules:
        
        * Must be greater than 0
        * Must not exceed ``originalDisputeAmount``
        * All submitted evidence will be applied only to defending this partial amount
        
        | Example: If dispute is EUR 100 and ``partialAmount`` is EUR 30, you're defending EUR 30 and accepting liability for EUR 70.

        Type: :class:`worldline.acquiring.sdk.v1.domain.amount_data.AmountData`
        """
        return self.__partial_amount

    @partial_amount.setter
    def partial_amount(self, value: Optional[AmountData]) -> None:
        self.__partial_amount = value

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
        dictionary = super(SubmitEvidenceRequest, self).to_dictionary()
        if self.document_ids is not None:
            dictionary['documentIds'] = []
            for element in self.document_ids:
                if element is not None:
                    dictionary['documentIds'].append(element.to_dictionary())
        if self.elaboration is not None:
            dictionary['elaboration'] = self.elaboration
        if self.include_entries is not None:
            dictionary['includeEntries'] = self.include_entries
        if self.partial_amount is not None:
            dictionary['partialAmount'] = self.partial_amount.to_dictionary()
        if self.user_id is not None:
            dictionary['userId'] = self.user_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SubmitEvidenceRequest':
        super(SubmitEvidenceRequest, self).from_dictionary(dictionary)
        if 'documentIds' in dictionary:
            if not isinstance(dictionary['documentIds'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['documentIds']))
            self.document_ids = []
            for element in dictionary['documentIds']:
                value = DisputeDocumentIdItem()
                self.document_ids.append(value.from_dictionary(element))
        if 'elaboration' in dictionary:
            self.elaboration = dictionary['elaboration']
        if 'includeEntries' in dictionary:
            self.include_entries = dictionary['includeEntries']
        if 'partialAmount' in dictionary:
            if not isinstance(dictionary['partialAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['partialAmount']))
            value = AmountData()
            self.partial_amount = value.from_dictionary(dictionary['partialAmount'])
        if 'userId' in dictionary:
            self.user_id = dictionary['userId']
        return self
