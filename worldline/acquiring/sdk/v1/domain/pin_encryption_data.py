# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional, cast

from worldline.acquiring.sdk.domain.data_object import DataObject


class PinEncryptionData(DataObject):

    __pin_encryption_type: Optional[str] = None

    @property
    def pin_encryption_type(self) -> str:
        """
        | Possible values are: AES_UKPT, DUKPT, ZPK.

        Type: str
        """
        return cast(str, self.__pin_encryption_type)

    @pin_encryption_type.setter
    def pin_encryption_type(self, value: str) -> None:
        self.__pin_encryption_type = value

    def to_dictionary(self) -> dict:
        dictionary = super(PinEncryptionData, self).to_dictionary()
        if self.pin_encryption_type is not None:
            dictionary['pinEncryptionType'] = self.pin_encryption_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'PinEncryptionData':
        super(PinEncryptionData, self).from_dictionary(dictionary)
        if 'pinEncryptionType' in dictionary:
            self.__pin_encryption_type = dictionary['pinEncryptionType']
        return self
