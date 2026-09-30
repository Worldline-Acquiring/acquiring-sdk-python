# -*- coding: utf-8 -*-
#
# This file was automatically generated.
#
from typing import Optional

from .dispute_case_with_entries import DisputeCaseWithEntries

from worldline.acquiring.sdk.domain.data_object import DataObject


class DisputeResponse(DataObject):

    __dispute: Optional[DisputeCaseWithEntries] = None
    __request_id: Optional[str] = None

    @property
    def dispute(self) -> Optional[DisputeCaseWithEntries]:
        """
        | A dispute represents a chargeback case. It contains details on the dispute and a history of entries that were done against the dispute during the lifecycle of the dispute.
        |
        | Each dispute has a unique ``disputeId`` that identifies it. You can use this ``disputeId`` to retrieve the details of the dispute and its history via the `Retrieve Dispute <#operation/getDispute>`_ endpoint, or to retrieve specific documents related to the dispute via the `Retrieve Dispute Document <#operation/getDisputeDocument>`_ endpoint.
        |
        | We return both the ``schemeReason``, which is the reason provided by the card scheme for the dispute, and the ``unifiedReason``, which is our mapping of the scheme reason to a unified reason that we use across all schemes. This allows you to easily filter disputes based on the ``unifiedReason``, while still having the ``schemeReason`` available for reference. The ``unifiedCategory`` is a high level category of the dispute reason, that we use to group similar ``unifiedReason`` values together.
        |
        | The ``disputeStatus`` field represents the current status of the dispute. The possible values for this field are specific to each card scheme, but we also provide a ``disputeStatusCategory`` field that groups the different ``disputeStatus`` values into a few high level categories that are consistent across all schemes. This allows you to easily filter disputes based on the ``disputeStatusCategory``, while still having the ``disputeStatus`` available for reference.
        |
        | The ``disputeStage`` field represents the current stage of the dispute in the dispute lifecycle. The possible values for this field represent the different stages that a dispute can be in during its lifecycle, such as "DISPUTE", "PRE_ARBITRATION", "ARBITRATION", etc.
        |
        | The ``originalDisputeAmount`` object represents the original amount of the dispute when it was first created. This amount can change during the lifecycle of the dispute, for example if the cardholder disputes only part of the original transaction amount, or if there are fees applied to the dispute. The ``merchantBalanceAmount`` field represents the current amount that's charged to or credited back to the merchant for this dispute. This amount can be different from the ``originalDisputeAmount`` due to partial disputes, fees, or if the dispute was challenged by the merchant and is currently being reviewed by the card scheme.
        |
        | The ``disputeReferences`` object contains a set of references related to the dispute, such as the acquirer dispute reference and the scheme dispute reference. These references can be used when communicating with the acquirer or the card scheme about the dispute.
        |
        | The ``DisputeDateTimeData`` object contains a set of date time fields related to the dispute, such as the opened date, response due date, closed date, etc. These fields can provide more context on the timeline of the dispute. When the ``disputeStatus`` is "EVIDENCE_REQUESTED", the ``responseDueDate`` field indicates the deadline to respond to the dispute.
        |
        | The ``originalTransactionData`` object contains data related to the original transaction that led to the dispute, such as transaction references, transaction amount, payment method data, etc. This information can be useful to understand the context of the dispute and to provide evidence when challenging the dispute.
        |
        | The ``merchantData`` object contains data related to the merchant involved in the dispute, such as merchant name, merchant category code, acquirer ID, etc. This information can also be useful to understand the context of the dispute and to provide evidence when challenging the dispute.
        |
        | Optionally the full history of entries for the dispute is included by setting the ``includeEntries`` parameter to ``true`` when retrieving the dispute details. Each entry in the history represents a step in the lifecycle of the dispute, such as when the dispute was opened, when evidence was requested by the acquirer, when evidence was provided by the merchant, when a credit adjustment was made by the acquirer, etc. The history is ordered from the oldest entry to the most recent one.

        Type: :class:`worldline.acquiring.sdk.v1.domain.dispute_case_with_entries.DisputeCaseWithEntries`
        """
        return self.__dispute

    @dispute.setter
    def dispute(self, value: Optional[DisputeCaseWithEntries]) -> None:
        self.__dispute = value

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
        dictionary = super(DisputeResponse, self).to_dictionary()
        if self.dispute is not None:
            dictionary['dispute'] = self.dispute.to_dictionary()
        if self.request_id is not None:
            dictionary['requestId'] = self.request_id
        return dictionary

    def from_dictionary(self, dictionary: dict) -> 'DisputeResponse':
        super(DisputeResponse, self).from_dictionary(dictionary)
        if 'dispute' in dictionary:
            if not isinstance(dictionary['dispute'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['dispute']))
            value = DisputeCaseWithEntries()
            self.dispute = value.from_dictionary(dictionary['dispute'])
        if 'requestId' in dictionary:
            self.request_id = dictionary['requestId']
        return self
