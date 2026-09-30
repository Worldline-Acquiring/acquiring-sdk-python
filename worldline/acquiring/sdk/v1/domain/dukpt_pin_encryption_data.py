# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .pin_encryption_data import PinEncryptionData


class DukptPinEncryptionData(PinEncryptionData):

    PIN_ENCRYPTION_TYPE = 'DUKPT'

    __key_serial_number: Optional[str] = None

    @property
    def pin_encryption_type(self) -> str:
        """
        | Possible values are: AES_UKPT, DUKPT, ZPK.

        Type: str
        """
        return self.PIN_ENCRYPTION_TYPE

    @property
    def key_serial_number(self) -> Optional[str]:
        """
        | Key Serial Number (KSN) if DUKPT encryption is used for the PIN block (3DES: 10 b, AES: 12 b)

        Type: str
        """
        return self.__key_serial_number

    @key_serial_number.setter
    def key_serial_number(self, value: Optional[str]) -> None:
        self.__key_serial_number = value

    def to_dictionary(self) -> dict:
        dictionary = super(DukptPinEncryptionData, self).to_dictionary()
        if self.key_serial_number is not None:
            dictionary['keySerialNumber'] = self.key_serial_number
        dictionary['pinEncryptionType'] = self.pin_encryption_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DukptPinEncryptionData':
        super(DukptPinEncryptionData, self).from_dictionary(dictionary)
        if 'keySerialNumber' in dictionary:
            self.key_serial_number = dictionary['keySerialNumber']
        return self
