# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .pin_encryption_data import PinEncryptionData


class AesUkptPinEncryptionData(PinEncryptionData):

    PIN_ENCRYPTION_TYPE = 'AES_UKPT'

    __key_generation: Optional[int] = None
    __random_value: Optional[str] = None

    @property
    def pin_encryption_type(self) -> str:
        """
        | Possible values are: AES_UKPT, DUKPT, ZPK.

        Type: str
        """
        return self.PIN_ENCRYPTION_TYPE

    @property
    def key_generation(self) -> Optional[int]:
        """
        | Generation/Version of the master key that was agreed with the partner

        Type: int
        """
        return self.__key_generation

    @key_generation.setter
    def key_generation(self, value: Optional[int]) -> None:
        self.__key_generation = value

    @property
    def random_value(self) -> Optional[str]:
        """
        | 16-byte binary random value to derive the PIN encryption session key

        Type: str
        """
        return self.__random_value

    @random_value.setter
    def random_value(self, value: Optional[str]) -> None:
        self.__random_value = value

    def to_dictionary(self) -> dict:
        dictionary = super(AesUkptPinEncryptionData, self).to_dictionary()
        if self.key_generation is not None:
            dictionary['keyGeneration'] = self.key_generation
        if self.random_value is not None:
            dictionary['randomValue'] = self.random_value
        dictionary['pinEncryptionType'] = self.pin_encryption_type
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'AesUkptPinEncryptionData':
        super(AesUkptPinEncryptionData, self).from_dictionary(dictionary)
        if 'keyGeneration' in dictionary:
            self.key_generation = dictionary['keyGeneration']
        if 'randomValue' in dictionary:
            self.random_value = dictionary['randomValue']
        return self
