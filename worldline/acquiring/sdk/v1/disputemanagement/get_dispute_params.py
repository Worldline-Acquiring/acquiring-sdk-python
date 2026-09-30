# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import List, Optional

from worldline.acquiring.sdk.communication.param_request import ParamRequest
from worldline.acquiring.sdk.communication.request_param import RequestParam


class GetDisputeParams(ParamRequest):
    """
    Query parameters for Retrieve Dispute

    See also https://docs.acquiring.worldline-solutions.com/api-reference#tag/Dispute-Management/operation/getDispute
    """

    __include_entries: Optional[bool] = None

    @property
    def include_entries(self) -> Optional[bool]:
        """
        | If true, the response will include the full history of dispute entries related to the dispute. False by default.

        Type: bool
        """
        return self.__include_entries

    @include_entries.setter
    def include_entries(self, value: Optional[bool]) -> None:
        self.__include_entries = value

    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[RequestParam]
        """
        result = []
        if self.include_entries is not None:
            result.append(RequestParam("includeEntries", str(self.include_entries)))
        return result
