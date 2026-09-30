# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .date_time_range import DateTimeRange
from .merchant_scope import MerchantScope
from .pagination_request import PaginationRequest

from worldline.acquiring.sdk.domain.data_object import DataObject


class SearchDisputeEntriesRequest(DataObject):

    __dispute_id: Optional[str] = None
    __entry_categories: Optional[List[str]] = None
    __entry_date_time: Optional[DateTimeRange] = None
    __entry_id: Optional[str] = None
    __entry_types: Optional[List[str]] = None
    __include_dispute_summary: Optional[bool] = None
    __merchant_scope: Optional[MerchantScope] = None
    __pagination: Optional[PaginationRequest] = None
    __sort_order: Optional[str] = None

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
    def entry_categories(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__entry_categories

    @entry_categories.setter
    def entry_categories(self, value: Optional[List[str]]) -> None:
        self.__entry_categories = value

    @property
    def entry_date_time(self) -> Optional[DateTimeRange]:
        """
        | A range of date time values, used to select disputes that have a date time field that falls within this range.
        |
        | **NOTE**: You can set either one or both of the lower and greater than properties to filter the results.

        Type: :class:`worldline.acquiring.sdk.v1.domain.date_time_range.DateTimeRange`
        """
        return self.__entry_date_time

    @entry_date_time.setter
    def entry_date_time(self, value: Optional[DateTimeRange]) -> None:
        self.__entry_date_time = value

    @property
    def entry_id(self) -> Optional[str]:
        """
        | The unique identifier for an dispute entry.

        Type: str
        """
        return self.__entry_id

    @entry_id.setter
    def entry_id(self, value: Optional[str]) -> None:
        self.__entry_id = value

    @property
    def entry_types(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__entry_types

    @entry_types.setter
    def entry_types(self, value: Optional[List[str]]) -> None:
        self.__entry_types = value

    @property
    def include_dispute_summary(self) -> Optional[bool]:
        """
        | If true, the summary of the dispute case will be included in the response for dispute entries search. The dispute case summary includes key information about the dispute case such as the current status, the reason for the dispute and the amount of the disputed transaction. This can be useful to provide context about the dispute case when searching for specific dispute entries.
        | False by default.

        Type: bool
        """
        return self.__include_dispute_summary

    @include_dispute_summary.setter
    def include_dispute_summary(self, value: Optional[bool]) -> None:
        self.__include_dispute_summary = value

    @property
    def merchant_scope(self) -> Optional[MerchantScope]:
        """
        | A set of fields to specify the scope of the search for disputes related to a specific merchant or set of merchants. The following options are available:
        
        * Search for disputes related to specific acquirers, by providing the ``acquirerIds`` field.
        * Search for disputes related to specific merchant groups, by providing the ``merchantRootIds`` field.
        * Search for disputes related to specific merchants, by providing the ``merchantIds`` field.
        
        | If no merchant scope is provided, disputes for all merchants that the API user has access to will be returned (that also match the other provided search criteria, if any).

        Type: :class:`worldline.acquiring.sdk.v1.domain.merchant_scope.MerchantScope`
        """
        return self.__merchant_scope

    @merchant_scope.setter
    def merchant_scope(self, value: Optional[MerchantScope]) -> None:
        self.__merchant_scope = value

    @property
    def pagination(self) -> Optional[PaginationRequest]:
        """
        | Pagination details for paginated responses.
        |
        | First request: Omit ``searchId``, set ``fromIndex``=0, ``pageSize``=20 Subsequent requests: Use ``searchId`` from previous response to maintain query context.
        |
        | Note: ``searchId`` expires after 24 hours. If you should perform your original search request again.

        Type: :class:`worldline.acquiring.sdk.v1.domain.pagination_request.PaginationRequest`
        """
        return self.__pagination

    @pagination.setter
    def pagination(self, value: Optional[PaginationRequest]) -> None:
        self.__pagination = value

    @property
    def sort_order(self) -> Optional[str]:
        """
        | The order in which to sort the dispute entries in the response. Can be either ascending (ASC) or descending (DESC). The sorting is done based on the ``entryDateTime`` field of the dispute entries, so when the sort order is ascending, the oldest entry is returned first and the newest entry is returned last. By default, the dispute entries are sorted in descending order.

        Type: str
        """
        return self.__sort_order

    @sort_order.setter
    def sort_order(self, value: Optional[str]) -> None:
        self.__sort_order = value

    def to_dictionary(self) -> dict:
        dictionary = super(SearchDisputeEntriesRequest, self).to_dictionary()
        if self.dispute_id is not None:
            dictionary['disputeId'] = self.dispute_id
        if self.entry_categories is not None:
            dictionary['entryCategories'] = []
            for element in self.entry_categories:
                if element is not None:
                    dictionary['entryCategories'].append(element)
        if self.entry_date_time is not None:
            dictionary['entryDateTime'] = self.entry_date_time.to_dictionary()
        if self.entry_id is not None:
            dictionary['entryId'] = self.entry_id
        if self.entry_types is not None:
            dictionary['entryTypes'] = []
            for element in self.entry_types:
                if element is not None:
                    dictionary['entryTypes'].append(element)
        if self.include_dispute_summary is not None:
            dictionary['includeDisputeSummary'] = self.include_dispute_summary
        if self.merchant_scope is not None:
            dictionary['merchantScope'] = self.merchant_scope.to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.sort_order is not None:
            dictionary['sortOrder'] = self.sort_order
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SearchDisputeEntriesRequest':
        super(SearchDisputeEntriesRequest, self).from_dictionary(dictionary)
        if 'disputeId' in dictionary:
            self.dispute_id = dictionary['disputeId']
        if 'entryCategories' in dictionary:
            if not isinstance(dictionary['entryCategories'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entryCategories']))
            self.entry_categories = []
            for element in dictionary['entryCategories']:
                self.entry_categories.append(element)
        if 'entryDateTime' in dictionary:
            if not isinstance(dictionary['entryDateTime'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['entryDateTime']))
            value = DateTimeRange()
            self.entry_date_time = value.from_dictionary(dictionary['entryDateTime'])
        if 'entryId' in dictionary:
            self.entry_id = dictionary['entryId']
        if 'entryTypes' in dictionary:
            if not isinstance(dictionary['entryTypes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['entryTypes']))
            self.entry_types = []
            for element in dictionary['entryTypes']:
                self.entry_types.append(element)
        if 'includeDisputeSummary' in dictionary:
            self.include_dispute_summary = dictionary['includeDisputeSummary']
        if 'merchantScope' in dictionary:
            if not isinstance(dictionary['merchantScope'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantScope']))
            value = MerchantScope()
            self.merchant_scope = value.from_dictionary(dictionary['merchantScope'])
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = PaginationRequest()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'sortOrder' in dictionary:
            self.sort_order = dictionary['sortOrder']
        return self
