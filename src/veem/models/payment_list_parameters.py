from oveem.models.base import Base

from oveem.constants import (
    Direction,
    PaymentStatus,
    PaymentSortField,
    SortOrder
)

from oveem.utils import deseralize

class PaymentListParameters(Base):
    def __init__(self,
                 direction=None,
                 paymentIds=[],
                 status=[],
                 sortParameters={},
                 pageNumber=0,
                 pageSize=1,
                 **kwargs):

        self._validate_constants(Direction, direction)
        self._validate_constants(PaymentStatus, status)
        self._validate_constants((PaymentSortField, SortOrder), sortParameters)

        self.direction = direction
        self.paymentIds = paymentIds
        self.status = status
        self.sortParameters = sortParameters
        self.pageNumber = pageNumber
        self.pageSize = pageSize
