# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeDateTimeData(DataObject):

    __closed_date_time: Optional[str] = None
    __last_status_changed_date_time: Optional[str] = None
    __opened_date_time: Optional[str] = None
    __response_due_date: Optional[date] = None

    @property
    def closed_date_time(self) -> Optional[str]:
        """
        | The date and time when the dispute was closed, in ISO 8601 format, but without the timezone designator. Only present if the dispute is closed.

        Type: str
        """
        return self.__closed_date_time

    @closed_date_time.setter
    def closed_date_time(self, value: Optional[str]) -> None:
        self.__closed_date_time = value

    @property
    def last_status_changed_date_time(self) -> Optional[str]:
        """
        | The date and time when the status of the dispute was last updated, in ISO 8601 format, but without the timezone designator. When the dispute case is first created the value will be equal to the ``OpenedDateTime`` property. As dispute process continues, this value changes.

        Type: str
        """
        return self.__last_status_changed_date_time

    @last_status_changed_date_time.setter
    def last_status_changed_date_time(self, value: Optional[str]) -> None:
        self.__last_status_changed_date_time = value

    @property
    def opened_date_time(self) -> Optional[str]:
        """
        | The date and time when the dispute was opened, in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__opened_date_time

    @opened_date_time.setter
    def opened_date_time(self, value: Optional[str]) -> None:
        self.__opened_date_time = value

    @property
    def response_due_date(self) -> Optional[date]:
        """
        | The date when a response to the dispute is due. This field is typically relevant when the ``disputeStatus`` is "EVIDENCE_REQUESTED", to indicate the deadline to respond to the dispute.

        Type: date
        """
        return self.__response_due_date

    @response_due_date.setter
    def response_due_date(self, value: Optional[date]) -> None:
        self.__response_due_date = value

    def to_dictionary(self) -> dict:
        dictionary = super(DisputeDateTimeData, self).to_dictionary()
        if self.closed_date_time is not None:
            dictionary['closedDateTime'] = self.closed_date_time
        if self.last_status_changed_date_time is not None:
            dictionary['lastStatusChangedDateTime'] = self.last_status_changed_date_time
        if self.opened_date_time is not None:
            dictionary['openedDateTime'] = self.opened_date_time
        if self.response_due_date is not None:
            dictionary['responseDueDate'] = DataObject.format_date(self.response_due_date)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeDateTimeData':
        super(DisputeDateTimeData, self).from_dictionary(dictionary)
        if 'closedDateTime' in dictionary:
            self.closed_date_time = dictionary['closedDateTime']
        if 'lastStatusChangedDateTime' in dictionary:
            self.last_status_changed_date_time = dictionary['lastStatusChangedDateTime']
        if 'openedDateTime' in dictionary:
            self.opened_date_time = dictionary['openedDateTime']
        if 'responseDueDate' in dictionary:
            self.response_due_date = DataObject.parse_date(dictionary['responseDueDate'])
        return self
