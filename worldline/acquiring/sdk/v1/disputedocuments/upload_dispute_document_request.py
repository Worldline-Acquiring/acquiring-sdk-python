# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.communication.multipart_form_data_object import MultipartFormDataObject
from worldline.acquiring.sdk.communication.multipart_form_data_request import MultipartFormDataRequest
from worldline.acquiring.sdk.domain.uploadable_file import UploadableFile


class UploadDisputeDocumentRequest(MultipartFormDataRequest):
    """
    Multipart/form-data parameters for Upload Dispute Document

    See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Documents/operation/uploadDisputeDocument
    """

    __file: Optional[UploadableFile] = None

    @property
    def file(self) -> Optional[UploadableFile]:
        """
        | The file to upload as evidence. The file must be provided in the multipart form data of the request.

        Type: :class:`worldline.acquiring.sdk.domain.uploadable_file.UploadableFile`
        """
        return self.__file

    @file.setter
    def file(self, value: Optional[UploadableFile]) -> None:
        self.__file = value

    def to_multipart_form_data_object(self) -> MultipartFormDataObject:
        """
        :return: :class:`worldline.acquiring.sdk.communication.multipart_form_data_object.MultipartFormDataObject`
        """
        result = MultipartFormDataObject()
        if self.file is not None:
            result.add_file("file", self.file)
        return result
