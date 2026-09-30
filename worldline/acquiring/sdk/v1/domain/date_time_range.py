# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from worldline.acquiring.sdk.domain.data_object import DataObject


class DateTimeRange(DataObject):

    __greater: Optional[str] = None
    __greater_equal: Optional[str] = None
    __lower: Optional[str] = None
    __lower_equal: Optional[str] = None

    @property
    def greater(self) -> Optional[str]:
        """
        | A date-time value that can be used in search criteria to filter results to only include items with a date-time greater to the specified value (after). The date-time is in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__greater

    @greater.setter
    def greater(self, value: Optional[str]) -> None:
        self.__greater = value

    @property
    def greater_equal(self) -> Optional[str]:
        """
        | A date-time value that can be used in search criteria to filter results to only include items with a date-time greater than or equal to the specified value (equal or after). The date-time is in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__greater_equal

    @greater_equal.setter
    def greater_equal(self, value: Optional[str]) -> None:
        self.__greater_equal = value

    @property
    def lower(self) -> Optional[str]:
        """
        | A date-time value that can be used in search criteria to filter results to only include items with a date-time lower to the specified value (before). The date-time is in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__lower

    @lower.setter
    def lower(self, value: Optional[str]) -> None:
        self.__lower = value

    @property
    def lower_equal(self) -> Optional[str]:
        """
        | A date-time value that can be used in search criteria to filter results to only include items with a date-time lower than or equal to the specified value (equal or before). The date-time is in ISO 8601 format, but without the timezone designator.

        Type: str
        """
        return self.__lower_equal

    @lower_equal.setter
    def lower_equal(self, value: Optional[str]) -> None:
        self.__lower_equal = value

    def to_dictionary(self) -> dict:
        dictionary = super(DateTimeRange, self).to_dictionary()
        if self.greater is not None:
            dictionary['greater'] = self.greater
        if self.greater_equal is not None:
            dictionary['greaterEqual'] = self.greater_equal
        if self.lower is not None:
            dictionary['lower'] = self.lower
        if self.lower_equal is not None:
            dictionary['lowerEqual'] = self.lower_equal
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DateTimeRange':
        super(DateTimeRange, self).from_dictionary(dictionary)
        if 'greater' in dictionary:
            self.greater = dictionary['greater']
        if 'greaterEqual' in dictionary:
            self.greater_equal = dictionary['greaterEqual']
        if 'lower' in dictionary:
            self.lower = dictionary['lower']
        if 'lowerEqual' in dictionary:
            self.lower_equal = dictionary['lowerEqual']
        return self
