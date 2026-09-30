# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from datetime import date
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DateRange(DataObject):

    __greater_equal: Optional[date] = None
    __lower_equal: Optional[date] = None

    @property
    def greater_equal(self) -> Optional[date]:
        """
        | A date value that can be used in search criteria to filter results to only include items with a date greater than or equal to the specified value (equal or after). The date is in ISO 8601 format.

        Type: date
        """
        return self.__greater_equal

    @greater_equal.setter
    def greater_equal(self, value: Optional[date]) -> None:
        self.__greater_equal = value

    @property
    def lower_equal(self) -> Optional[date]:
        """
        | A date value that can be used in search criteria to filter results to only include items with a date lower than the specified value (equal or before). The date is in ISO 8601 format.

        Type: date
        """
        return self.__lower_equal

    @lower_equal.setter
    def lower_equal(self, value: Optional[date]) -> None:
        self.__lower_equal = value

    def to_dictionary(self) -> dict:
        dictionary = super(DateRange, self).to_dictionary()
        if self.greater_equal is not None:
            dictionary['greaterEqual'] = DataObject.format_date(self.greater_equal)
        if self.lower_equal is not None:
            dictionary['lowerEqual'] = DataObject.format_date(self.lower_equal)
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DateRange':
        super(DateRange, self).from_dictionary(dictionary)
        if 'greaterEqual' in dictionary:
            self.greater_equal = DataObject.parse_date(dictionary['greaterEqual'])
        if 'lowerEqual' in dictionary:
            self.lower_equal = DataObject.parse_date(dictionary['lowerEqual'])
        return self
