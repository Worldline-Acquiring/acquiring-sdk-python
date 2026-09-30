# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from .date_range import DateRange
from .date_time_range import DateTimeRange
from .merchant_scope import MerchantScope
from .pagination_request import PaginationRequest

from worldline.acquiring.sdk.domain.data_object import DataObject


class SearchDisputesRequest(DataObject):

    __acquirer_dispute_reference: Optional[str] = None
    __acquirer_reference_number: Optional[str] = None
    __closed_date_time: Optional[DateTimeRange] = None
    __dispute_id: Optional[str] = None
    __dispute_stages: Optional[List[str]] = None
    __dispute_status_categories: Optional[List[str]] = None
    __is_open: Optional[bool] = None
    __last_status_changed_date_time: Optional[DateTimeRange] = None
    __merchant_reference: Optional[str] = None
    __merchant_scope: Optional[MerchantScope] = None
    __opened_date_time: Optional[DateTimeRange] = None
    __pagination: Optional[PaginationRequest] = None
    __payment_id: Optional[str] = None
    __response_due_date: Optional[DateRange] = None
    __schemes: Optional[List[str]] = None
    __sort_by: Optional[str] = None
    __sort_order: Optional[str] = None
    __unified_categories: Optional[List[str]] = None

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
    def acquirer_reference_number(self) -> Optional[str]:
        """
        | Acquirer reference number (ARN) for transaction

        Type: str
        """
        return self.__acquirer_reference_number

    @acquirer_reference_number.setter
    def acquirer_reference_number(self, value: Optional[str]) -> None:
        self.__acquirer_reference_number = value

    @property
    def closed_date_time(self) -> Optional[DateTimeRange]:
        """
        | A range of date time values, used to select disputes that have a date time field that falls within this range.
        |
        | **NOTE**: You can set either one or both of the lower and greater than properties to filter the results.

        Type: :class:`worldline.acquiring.sdk.v1.domain.date_time_range.DateTimeRange`
        """
        return self.__closed_date_time

    @closed_date_time.setter
    def closed_date_time(self, value: Optional[DateTimeRange]) -> None:
        self.__closed_date_time = value

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
    def dispute_stages(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__dispute_stages

    @dispute_stages.setter
    def dispute_stages(self, value: Optional[List[str]]) -> None:
        self.__dispute_stages = value

    @property
    def dispute_status_categories(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__dispute_status_categories

    @dispute_status_categories.setter
    def dispute_status_categories(self, value: Optional[List[str]]) -> None:
        self.__dispute_status_categories = value

    @property
    def is_open(self) -> Optional[bool]:
        """
        | Indicates whether the dispute is open or closed. An open dispute is a dispute that's still in the process of being resolved, while a closed dispute is a dispute that has been resolved.

        Type: bool
        """
        return self.__is_open

    @is_open.setter
    def is_open(self, value: Optional[bool]) -> None:
        self.__is_open = value

    @property
    def last_status_changed_date_time(self) -> Optional[DateTimeRange]:
        """
        | A range of date time values, used to select disputes that have a date time field that falls within this range.
        |
        | **NOTE**: You can set either one or both of the lower and greater than properties to filter the results.

        Type: :class:`worldline.acquiring.sdk.v1.domain.date_time_range.DateTimeRange`
        """
        return self.__last_status_changed_date_time

    @last_status_changed_date_time.setter
    def last_status_changed_date_time(self, value: Optional[DateTimeRange]) -> None:
        self.__last_status_changed_date_time = value

    @property
    def merchant_reference(self) -> Optional[str]:
        """
        | Reference for the transaction to allow the merchant to reconcile their payments in our report files and in their disputes.
        | It is advised to submit a unique value per transaction.
        | The value is returned in the baseTrxType/addlMercData element of the MRX file.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value: Optional[str]) -> None:
        self.__merchant_reference = value

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
    def opened_date_time(self) -> Optional[DateTimeRange]:
        """
        | A range of date time values, used to select disputes that have a date time field that falls within this range.
        |
        | **NOTE**: You can set either one or both of the lower and greater than properties to filter the results.

        Type: :class:`worldline.acquiring.sdk.v1.domain.date_time_range.DateTimeRange`
        """
        return self.__opened_date_time

    @opened_date_time.setter
    def opened_date_time(self, value: Optional[DateTimeRange]) -> None:
        self.__opened_date_time = value

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
    def payment_id(self) -> Optional[str]:
        """
        | The unique identifier for the original payment transaction that resulted in the dispute. Depending on the interface used for the original transaction different values are returned. If the original transaction was made through the Acquiring API, the ``paymentId`` from the original transaction is returned.

        Type: str
        """
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value: Optional[str]) -> None:
        self.__payment_id = value

    @property
    def response_due_date(self) -> Optional[DateRange]:
        """
        | A range of date values, used to select disputes that have a date field that falls within this range.
        |
        | **NOTE**: You can set either one or both of the properties to filter the results.

        Type: :class:`worldline.acquiring.sdk.v1.domain.date_range.DateRange`
        """
        return self.__response_due_date

    @response_due_date.setter
    def response_due_date(self, value: Optional[DateRange]) -> None:
        self.__response_due_date = value

    @property
    def schemes(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__schemes

    @schemes.setter
    def schemes(self, value: Optional[List[str]]) -> None:
        self.__schemes = value

    @property
    def sort_by(self) -> Optional[str]:
        """
        | The field by which to sort the search results. This can be any of the date-time fields in the dispute resource, such as ``openedDateTime``, ``closedDateTime``, ``lastStatusChangedDateTime`` or ``responseDueDate``.

        Type: str
        """
        return self.__sort_by

    @sort_by.setter
    def sort_by(self, value: Optional[str]) -> None:
        self.__sort_by = value

    @property
    def sort_order(self) -> Optional[str]:
        """
        | The order in which to sort the search results. Can be either ascending (ASC) or descending (DESC).

        Type: str
        """
        return self.__sort_order

    @sort_order.setter
    def sort_order(self, value: Optional[str]) -> None:
        self.__sort_order = value

    @property
    def unified_categories(self) -> Optional[List[str]]:
        """
        Type: list[str]
        """
        return self.__unified_categories

    @unified_categories.setter
    def unified_categories(self, value: Optional[List[str]]) -> None:
        self.__unified_categories = value

    def to_dictionary(self) -> dict:
        dictionary = super(SearchDisputesRequest, self).to_dictionary()
        if self.acquirer_dispute_reference is not None:
            dictionary['acquirerDisputeReference'] = self.acquirer_dispute_reference
        if self.acquirer_reference_number is not None:
            dictionary['acquirerReferenceNumber'] = self.acquirer_reference_number
        if self.closed_date_time is not None:
            dictionary['closedDateTime'] = self.closed_date_time.to_dictionary()
        if self.dispute_id is not None:
            dictionary['disputeId'] = self.dispute_id
        if self.dispute_stages is not None:
            dictionary['disputeStages'] = []
            for element in self.dispute_stages:
                if element is not None:
                    dictionary['disputeStages'].append(element)
        if self.dispute_status_categories is not None:
            dictionary['disputeStatusCategories'] = []
            for element in self.dispute_status_categories:
                if element is not None:
                    dictionary['disputeStatusCategories'].append(element)
        if self.is_open is not None:
            dictionary['isOpen'] = self.is_open
        if self.last_status_changed_date_time is not None:
            dictionary['lastStatusChangedDateTime'] = self.last_status_changed_date_time.to_dictionary()
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.merchant_scope is not None:
            dictionary['merchantScope'] = self.merchant_scope.to_dictionary()
        if self.opened_date_time is not None:
            dictionary['openedDateTime'] = self.opened_date_time.to_dictionary()
        if self.pagination is not None:
            dictionary['pagination'] = self.pagination.to_dictionary()
        if self.payment_id is not None:
            dictionary['paymentId'] = self.payment_id
        if self.response_due_date is not None:
            dictionary['responseDueDate'] = self.response_due_date.to_dictionary()
        if self.schemes is not None:
            dictionary['schemes'] = []
            for element in self.schemes:
                if element is not None:
                    dictionary['schemes'].append(element)
        if self.sort_by is not None:
            dictionary['sortBy'] = self.sort_by
        if self.sort_order is not None:
            dictionary['sortOrder'] = self.sort_order
        if self.unified_categories is not None:
            dictionary['unifiedCategories'] = []
            for element in self.unified_categories:
                if element is not None:
                    dictionary['unifiedCategories'].append(element)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'SearchDisputesRequest':
        super(SearchDisputesRequest, self).from_dictionary(dictionary)
        if 'acquirerDisputeReference' in dictionary:
            self.acquirer_dispute_reference = dictionary['acquirerDisputeReference']
        if 'acquirerReferenceNumber' in dictionary:
            self.acquirer_reference_number = dictionary['acquirerReferenceNumber']
        if 'closedDateTime' in dictionary:
            if not isinstance(dictionary['closedDateTime'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['closedDateTime']))
            value = DateTimeRange()
            self.closed_date_time = value.from_dictionary(dictionary['closedDateTime'])
        if 'disputeId' in dictionary:
            self.dispute_id = dictionary['disputeId']
        if 'disputeStages' in dictionary:
            if not isinstance(dictionary['disputeStages'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['disputeStages']))
            self.dispute_stages = []
            for element in dictionary['disputeStages']:
                self.dispute_stages.append(element)
        if 'disputeStatusCategories' in dictionary:
            if not isinstance(dictionary['disputeStatusCategories'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['disputeStatusCategories']))
            self.dispute_status_categories = []
            for element in dictionary['disputeStatusCategories']:
                self.dispute_status_categories.append(element)
        if 'isOpen' in dictionary:
            self.is_open = dictionary['isOpen']
        if 'lastStatusChangedDateTime' in dictionary:
            if not isinstance(dictionary['lastStatusChangedDateTime'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['lastStatusChangedDateTime']))
            value = DateTimeRange()
            self.last_status_changed_date_time = value.from_dictionary(dictionary['lastStatusChangedDateTime'])
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'merchantScope' in dictionary:
            if not isinstance(dictionary['merchantScope'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantScope']))
            value = MerchantScope()
            self.merchant_scope = value.from_dictionary(dictionary['merchantScope'])
        if 'openedDateTime' in dictionary:
            if not isinstance(dictionary['openedDateTime'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['openedDateTime']))
            value = DateTimeRange()
            self.opened_date_time = value.from_dictionary(dictionary['openedDateTime'])
        if 'pagination' in dictionary:
            if not isinstance(dictionary['pagination'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['pagination']))
            value = PaginationRequest()
            self.pagination = value.from_dictionary(dictionary['pagination'])
        if 'paymentId' in dictionary:
            self.payment_id = dictionary['paymentId']
        if 'responseDueDate' in dictionary:
            if not isinstance(dictionary['responseDueDate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['responseDueDate']))
            value = DateRange()
            self.response_due_date = value.from_dictionary(dictionary['responseDueDate'])
        if 'schemes' in dictionary:
            if not isinstance(dictionary['schemes'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['schemes']))
            self.schemes = []
            for element in dictionary['schemes']:
                self.schemes.append(element)
        if 'sortBy' in dictionary:
            self.sort_by = dictionary['sortBy']
        if 'sortOrder' in dictionary:
            self.sort_order = dictionary['sortOrder']
        if 'unifiedCategories' in dictionary:
            if not isinstance(dictionary['unifiedCategories'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['unifiedCategories']))
            self.unified_categories = []
            for element in dictionary['unifiedCategories']:
                self.unified_categories.append(element)
        return self
