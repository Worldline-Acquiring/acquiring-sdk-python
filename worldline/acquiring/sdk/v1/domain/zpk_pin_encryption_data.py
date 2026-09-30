# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .pin_encryption_data import PinEncryptionData


class ZpkPinEncryptionData(PinEncryptionData):

    PIN_ENCRYPTION_TYPE = 'ZPK'

    __zone_pin_key_id: Optional[str] = None

    @property
    def pin_encryption_type(self) -> str:
        """
        | Possible values are: AES_UKPT, DUKPT, ZPK.

        Type: str
        """
        return self.PIN_ENCRYPTION_TYPE

    @property
    def zone_pin_key_id(self) -> Optional[str]:
        """
        | ID of the Zone PIN Key if ZPK encryption is used for the PIN block

        Type: str
        """
        return self.__zone_pin_key_id

    @zone_pin_key_id.setter
    def zone_pin_key_id(self, value: Optional[str]) -> None:
        self.__zone_pin_key_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(ZpkPinEncryptionData, self).to_dictionary()
        if self.zone_pin_key_id is not None:
            dictionary['zonePinKeyId'] = self.zone_pin_key_id
        dictionary['pinEncryptionType'] = self.pin_encryption_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'ZpkPinEncryptionData':
        super(ZpkPinEncryptionData, self).from_dictionary(dictionary)
        if 'zonePinKeyId' in dictionary:
            self.zone_pin_key_id = dictionary['zonePinKeyId']
        return self
