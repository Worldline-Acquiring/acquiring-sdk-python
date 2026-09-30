# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class AcceptDisputeLiabilityRequest(DataObject):

    __include_entries: Optional[bool] = None
    __message_text: Optional[str] = None
    __user_id: Optional[str] = None

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
        dictionary = super(AcceptDisputeLiabilityRequest, self).to_dictionary()
        if self.include_entries is not None:
            dictionary['includeEntries'] = self.include_entries
        if self.message_text is not None:
            dictionary['messageText'] = self.message_text
        if self.user_id is not None:
            dictionary['userId'] = self.user_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AcceptDisputeLiabilityRequest':
        super(AcceptDisputeLiabilityRequest, self).from_dictionary(dictionary)
        if 'includeEntries' in dictionary:
            self.include_entries = dictionary['includeEntries']
        if 'messageText' in dictionary:
            self.message_text = dictionary['messageText']
        if 'userId' in dictionary:
            self.user_id = dictionary['userId']
        return self
