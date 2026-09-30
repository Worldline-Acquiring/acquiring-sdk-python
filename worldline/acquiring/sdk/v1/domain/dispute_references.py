# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeReferences(DataObject):

    __acquirer_dispute_reference: Optional[str] = None
    __scheme_dispute_reference: Optional[str] = None

    @property
    def acquirer_dispute_reference(self) -> Optional[str]:
        """
        | The reference provided by the acquirer for the dispute.

        Type: str
        """
        return self.__acquirer_dispute_reference

    @acquirer_dispute_reference.setter
    def acquirer_dispute_reference(self, value: Optional[str]) -> None:
        self.__acquirer_dispute_reference = value

    @property
    def scheme_dispute_reference(self) -> Optional[str]:
        """
        | The reference provided by the card scheme for the dispute.

        Type: str
        """
        return self.__scheme_dispute_reference

    @scheme_dispute_reference.setter
    def scheme_dispute_reference(self, value: Optional[str]) -> None:
        self.__scheme_dispute_reference = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeReferences, self).to_dictionary()
        if self.acquirer_dispute_reference is not None:
            dictionary['acquirerDisputeReference'] = self.acquirer_dispute_reference
        if self.scheme_dispute_reference is not None:
            dictionary['schemeDisputeReference'] = self.scheme_dispute_reference
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeReferences':
        super(DisputeReferences, self).from_dictionary(dictionary)
        if 'acquirerDisputeReference' in dictionary:
            self.acquirer_dispute_reference = dictionary['acquirerDisputeReference']
        if 'schemeDisputeReference' in dictionary:
            self.scheme_dispute_reference = dictionary['schemeDisputeReference']
        return self
