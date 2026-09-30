# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeDocumentIdItem(DataObject):

    __document_id: Optional[str] = None

    @property
    def document_id(self) -> Optional[str]:
        """
        | The unique identifier of a document submitted as evidence for the dispute case, if applicable.

        Type: str
        """
        return self.__document_id

    @document_id.setter
    def document_id(self, value: Optional[str]) -> None:
        self.__document_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeDocumentIdItem, self).to_dictionary()
        if self.document_id is not None:
            dictionary['documentId'] = self.document_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeDocumentIdItem':
        super(DisputeDocumentIdItem, self).from_dictionary(dictionary)
        if 'documentId' in dictionary:
            self.document_id = dictionary['documentId']
        return self
