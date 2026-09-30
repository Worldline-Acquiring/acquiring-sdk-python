# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .dispute_case import DisputeCase
from .pagination_response import PaginationResponse

from worldline.acquiring.sdk.domain.data_object import DataObject


class SearchDisputesResponse(DataObject):

    __disputes: Optional[List[DisputeCase]] = None
    __pagination: Optional[PaginationResponse] = None
    __request_id: Optional[str] = None

    @property
    def disputes(self) -> Optional[List[DisputeCase]]:
        """
        | A list of dispute cases matching the provided search criteria. Each dispute case contains the full details of the dispute, but without the full history of entries for the dispute. These can be retrieved by setting the ``includeEntries`` parameter to true when using the `Retrieve Dispute <#operation/getDispute>`_ endpoint.

        Type: list[:class:`worldline.acquiring.sdk.v1.domain.dispute_case.DisputeCase`]
        """
        return self.__disputes

    @disputes.setter
    def disputes(self, value: Optional[List[DisputeCase]]) -> None:
        self.__disputes = value

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
        dictionary = super(SearchDisputesResponse, self).to_dictionary()
        if self.disputes is not None:
            dictionary['disputes'] = []
            for element in self.disputes:
                if element is not None:
                    dictionary['disputes'].append(element.to_dictionary())
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.request_id is not None:
            dictionary['requestId'] = self.request_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SearchDisputesResponse':
        super(SearchDisputesResponse, self).from_dictionary(dictionary)
        if 'disputes' in dictionary:
            if not isinstance(dictionary['disputes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['disputes']))
            self.disputes = []
            for element in dictionary['disputes']:
                value = DisputeCase()
                self.disputes.append(value.from_dictionary(element))
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = PaginationResponse()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
