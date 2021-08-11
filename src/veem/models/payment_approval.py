
from oveem.models.base import Base
from oveem.models.approver import Approver

from oveem.utils import deseralize
from oveem.constants import ApprovalStatus

class PaymentApproval(Base):
    def __init__(self,
                 approversCompleted=None,
                 status=None,
                 approversRequired=None,
                 approvers=[],
                 **kwargs):

        self._validate_constants(ApprovalStatus, status)

        self.approversCompleted = approversCompleted
        self.status = status
        self.approversRequired = approversRequired
        self.approvers = [deseralize(Approver,
                                     apr) for apr in approvers]
