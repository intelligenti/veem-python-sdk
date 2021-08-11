from odooveem.models.base import Base
from odooveem.models.amount import Amount

from odooveem.utils import deseralize

class PushPaymentInfo(Base):
    def __init__(self,
                 amount=None,
                 reference=None,
                 pushPaymentInfo=None,
                 **kwargs):

        self.amount = deseralize(Amount, amount)
        self.reference = reference
        self.pushPaymentInfo = pushPaymentInfo
