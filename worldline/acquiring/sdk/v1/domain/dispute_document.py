# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeDocument(DataObject):

    __document_id: Optional[str] = None
    __file_name: Optional[str] = None
    __mime_type: Optional[str] = None

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
    def file_name(self) -> Optional[str]:
        """
        | The name of the file submitted as evidence for the dispute case, if applicable.

        Type: str
        """
        return self.__file_name

    @file_name.setter
    def file_name(self, value: Optional[str]) -> None:
        self.__file_name = value

    @property
    def mime_type(self) -> Optional[str]:
        """
        | The MIME type of the file submitted as evidence for the dispute case, if applicable.
        |
        | Possible values are:
        
        * ``application/pdf``
        * ``image/jpeg``
        * ``image/jpg``
        * ``image/png``

        Type: str
        """
        return self.__mime_type

    @mime_type.setter
    def mime_type(self, value: Optional[str]) -> None:
        self.__mime_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeDocument, self).to_dictionary()
        if self.document_id is not None:
            dictionary['documentId'] = self.document_id
        if self.file_name is not None:
            dictionary['fileName'] = self.file_name
        if self.mime_type is not None:
            dictionary['mimeType'] = self.mime_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeDocument':
        super(DisputeDocument, self).from_dictionary(dictionary)
        if 'documentId' in dictionary:
            self.document_id = dictionary['documentId']
        if 'fileName' in dictionary:
            self.file_name = dictionary['fileName']
        if 'mimeType' in dictionary:
            self.mime_type = dictionary['mimeType']
        return self
