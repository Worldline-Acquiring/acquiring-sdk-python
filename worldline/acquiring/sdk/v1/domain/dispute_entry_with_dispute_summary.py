# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .dispute_entry import DisputeEntry
from .dispute_summary import DisputeSummary


class DisputeEntryWithDisputeSummary(DisputeEntry):

    __dispute_id: Optional[str] = None
    __dispute_summary: Optional[DisputeSummary] = None

    @property
    def dispute_id(self) -> Optional[str]:
        """
        | The unique identifier for a dispute.

        Type: str
        """
        return self.__dispute_id

    @dispute_id.setter
    def dispute_id(self, value: Optional[str]) -> None:
        self.__dispute_id = value

    @property
    def dispute_summary(self) -> Optional[DisputeSummary]:
        """
        | A summary of the dispute case, returned in the search results when searching for dispute
        | entries. This is only returned when explicitly requested via the ``includeDisputeSummary`` property is set to ``true`` in the request.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_summary.DisputeSummary`
        """
        return self.__dispute_summary

    @dispute_summary.setter
    def dispute_summary(self, value: Optional[DisputeSummary]) -> None:
        self.__dispute_summary = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeEntryWithDisputeSummary, self).to_dictionary()
        if self.dispute_id is not None:
            dictionary['disputeId'] = self.dispute_id
        if self.dispute_summary is not None:
            dictionary['disputeSummary'] = self.dispute_summary.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeEntryWithDisputeSummary':
        super(DisputeEntryWithDisputeSummary, self).from_dictionary(dictionary)
        if 'disputeId' in dictionary:
            self.dispute_id = dictionary['disputeId']
        if 'disputeSummary' in dictionary:
            if not isinstance(dictionary['disputeSummary'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['disputeSummary']))
            value = DisputeSummary()
            self.dispute_summary = value.from_dictionary(dictionary['disputeSummary'])
        return self
