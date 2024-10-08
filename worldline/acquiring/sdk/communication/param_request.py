from abc import ABC, abstractmethod
from typing import List

from .request_param import RequestParam


class ParamRequest(ABC):
    """
    Represents a set of request parameters.
    """

    @abstractmethod
    def to_request_parameters(self) -> List[RequestParam]:
        """
        :return: list[:class:`worldline.acquiring.sdk.communication.RequestParam`] representing the HTTP request parameters
        """
        raise NotImplementedError
