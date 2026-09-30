# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .dispute_entry_with_dispute_summary import DisputeEntryWithDisputeSummary
from .pagination_response import PaginationResponse

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeEntryResources(DataObject):

    __dispute_entries: Optional[List[DisputeEntryWithDisputeSummary]] = None
    __pagination: Optional[PaginationResponse] = None
    __request_id: Optional[str] = None

    @property
    def dispute_entries(self) -> Optional[List[DisputeEntryWithDisputeSummary]]:
        """
        | A list of dispute entries matching the provided search criteria. Each entry documents a single event in the lifecycle of the dispute, such as when the dispute was opened, when evidence was requested by the acquirer, when evidence was provided by the merchant, when a credit adjustment was made by the acquirer, etc.
        |
        | Each entry has a category and type that indicate what kind of step it represents. The data elements can be different, depending on the entry type. For some steps more details are provided in a message text.
        |
        | For each entry, if there are documents related to it, a list of document metadata will be included in the ``documents`` field.
        |
        | Optionally a ``disputeSummary`` object can be included for each entry by setting the ``includeDisputeSummary`` parameter to ``true`` in the request of the `Search Dispute Entries <#operation/searchDisputeEntries>`_ endpoint. This summary contains key information on the dispute case that can be useful to understand the context of the entry, such as the current status and stage of the dispute, the type of dispute, the amount in dispute, the reason code, etc.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.dispute_entry_with_dispute_summary.DisputeEntryWithDisputeSummary`]
        """
        return self.__dispute_entries

    @dispute_entries.setter
    def dispute_entries(self, value: Optional[List[DisputeEntryWithDisputeSummary]]) -> None:
        self.__dispute_entries = value

    @property
    def pagination(self) -> Optional[PaginationResponse]:
        """
        | Pagination details for paginated responses.

        Type: :class:`worldline.acquiring.sdk.v1.domain.pagination_response.PaginationResponse`
        """
        return self.__pagination

    @pagination.setter
    def pagination(self, value: Optional[PaginationResponse]) -> None:
        self.__pagination = value

    @property
    def request_id(self) -> Optional[str]:
        """
        | The unique Worldline identifier for the request that resulted in this response.

        Type: str
        """
        return self.__request_id

    @request_id.setter
    def request_id(self, value: Optional[str]) -> None:
        self.__request_id = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeEntryResources, self).to_dictionary()
        if self.dispute_entries is not None:
            dictionary['disputeEntries'] = []
            for element in self.dispute_entries:
                if element is not None:
                    dictionary['disputeEntries'].append(element.to_dictionary())
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.request_id is not None:
            dictionary['requestId'] = self.request_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeEntryResources':
        super(DisputeEntryResources, self).from_dictionary(dictionary)
        if 'disputeEntries' in dictionary:
            if not isinstance(dictionary['disputeEntries'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['disputeEntries']))
            self.dispute_entries = []
            for element in dictionary['disputeEntries']:
                value = DisputeEntryWithDisputeSummary()
                self.dispute_entries.append(value.from_dictionary(element))
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = PaginationResponse()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
