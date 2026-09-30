# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .dispute_case import DisputeCase
from .dispute_entry import DisputeEntry


class DisputeCaseWithEntries(DisputeCase):

    __entries: Optional[List[DisputeEntry]] = None

    @property
    def entries(self) -> Optional[List[DisputeEntry]]:
        """
        | A list of entries that were done against the dispute during its lifecycle.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.dispute_entry.DisputeEntry`]
        """
        return self.__entries

    @entries.setter
    def entries(self, value: Optional[List[DisputeEntry]]) -> None:
        self.__entries = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeCaseWithEntries, self).to_dictionary()
        if self.entries is not None:
            dictionary['entries'] = []
            for element in self.entries:
                if element is not None:
                    dictionary['entries'].append(element.to_dictionary())
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeCaseWithEntries':
        super(DisputeCaseWithEntries, self).from_dictionary(dictionary)
        if 'entries' in dictionary:
            if not isinstance(dictionary['entries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entries']))
            self.entries = []
            for element in dictionary['entries']:
                value = DisputeEntry()
                self.entries.append(value.from_dictionary(element))
        return self
