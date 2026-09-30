# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .pin_encryption_data import PinEncryptionData

from worldline.acquiring.sdk.domain.data_object import DataObject


class OnlinePinData(DataObject):

    __encrypted_pin_block: Optional[str] = None
    __pin_block_format: Optional[int] = None
    __pin_encryption_data: Optional[PinEncryptionData] = None

    @property
    def encrypted_pin_block(self) -> Optional[str]:
        """
        | Encrypted data containing a PIN

        Type: str
        """
        return self.__encrypted_pin_block

    @encrypted_pin_block.setter
    def encrypted_pin_block(self, value: Optional[str]) -> None:
        self.__encrypted_pin_block = value

    @property
    def pin_block_format(self) -> Optional[int]:
        """
        | ISO 9564 based PIN block format.
        |
        | Worldline acquiring only supports the following format:
        
        * 4 - ISO-4
        
        | Bambora acquiring supports the following formats:
        
        * 0 - ISO 9564-1 Format 0 (Standard PIN block format with PAN XOR, commonly used with 3DES / DUKPT).
        * 1 - ISO 9564-1 Format 1 (PIN block with transaction sequence/random number).
        * 2 - ISO 9564-1 Format 2 (Primarily used for offline/smart cards).
        * 3 - ISO 9564-1 Format 3 (Similar to Format 0 with random fill digits).
        * 4 - ISO 9564-1 Format 4 (AES-256 encrypted PIN block format, required for modern Online PIN / Tap on Mobile CVM solutions).

        Type: int
        """
        return self.__pin_block_format

    @pin_block_format.setter
    def pin_block_format(self, value: Optional[int]) -> None:
        self.__pin_block_format = value

    @property
    def pin_encryption_data(self) -> Optional[PinEncryptionData]:
        """
        | PIN encryption details used for the ``encryptedPinBlock``.
        |
        | The following variants are supported:
        
        * AES_UKPT - Used in combination with Worldline acquirers
        * DUKPT - Used in combination with the Bambora acquirer
        * ZPK - Zone PIN Key, used in combination with the Bambora acquirer

        Type: :class:`worldline.acquiring.sdk.v1.domain.pin_encryption_data.PinEncryptionData`
        """
        return self.__pin_encryption_data

    @pin_encryption_data.setter
    def pin_encryption_data(self, value: Optional[PinEncryptionData]) -> None:
        self.__pin_encryption_data = value

    def to_dictionary(self) -> dict:
        dictionary = super(OnlinePinData, self).to_dictionary()
        if self.encrypted_pin_block is not None:
            dictionary['encryptedPinBlock'] = self.encrypted_pin_block
        if self.pin_block_format is not None:
            dictionary['pinBlockFormat'] = self.pin_block_format
        if self.pin_encryption_data is not None:
            dictionary['pinEncryptionData'] = self.pin_encryption_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'OnlinePinData':
        super(OnlinePinData, self).from_dictionary(dictionary)
        if 'encryptedPinBlock' in dictionary:
            self.encrypted_pin_block = dictionary['encryptedPinBlock']
        if 'pinBlockFormat' in dictionary:
            self.pin_block_format = dictionary['pinBlockFormat']
        if 'pinEncryptionData' in dictionary:
            if not isinstance(dictionary['pinEncryptionData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pinEncryptionData']))
            value = PinEncryptionData()
            self.pin_encryption_data = value.from_dictionary(dictionary['pinEncryptionData'])
        return self
