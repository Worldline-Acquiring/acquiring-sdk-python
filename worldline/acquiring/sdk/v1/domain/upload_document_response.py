# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class UploadDocumentResponse(DataObject):

    __document_id: Optional[str] = None
    __request_id: Optional[str] = None

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

    @property
    def request_id(self) -> Optional[str]:
        """
        | The unique Worldline identifier for the request that resulted in this response.

        Type: str
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value: Optional[str]) -> None:
        self.__request_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(UploadDocumentResponse, self).to_dictionary()
        if self.document_id is not None:
            dictionary['documentId'] = self.document_id
        if self.request_id is not None:
            dictionary['requestId'] = self.request_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'UploadDocumentResponse':
        super(UploadDocumentResponse, self).from_dictionary(dictionary)
        if 'documentId' in dictionary:
            self.document_id = dictionary['documentId']
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
