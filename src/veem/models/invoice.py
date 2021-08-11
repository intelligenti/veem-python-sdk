from odooveem.models.base import Base
from odooveem.models.amount import Amount
from odooveem.models.account import Account
from odooveem.models.attachment import Attachment
from odooveem.models.exchange_rate import ExchangeRate
from odooveem.models.payment_approval import PaymentApproval
from odooveem.models.push_payment_info import PushPaymentInfo

from odooveem.utils import deseralize
from odooveem.constants import InvoiceStatus

class Invoice(Base):
    def __init__(self,
                 id=None,
                 status=None,
                 exchangeRate=None,
                 timeCreated=None,
                 claimLink=None,
                 payer=None,
                 clientId=None,
                 amount=None,
                 notes=None,
                 externalInvoiceRefId=None,
                 ccEmails=[],
                 purposeOfPayment=None,
                 attachments=[],
                 exchangeRateQuoteId=None,
                 dueDate=None,
                 **kwargs):

        self._validate_constants(InvoiceStatus, status)

        self.id = id
        self.status = status
        self.exchangeRate = deseralize(ExchangeRate, exchangeRate)
        self.timeCreated = timeCreated
        self.claimLink = claimLink
        self.payer = deseralize(Account, payer)
        self.clientId = clientId
        self.amount = deseralize(Amount, amount)
        self.notes = notes
        self.externalInvoiceRefId = externalInvoiceRefId
        self.ccEmails = ccEmails
        self.purposeOfPayment = purposeOfPayment
        self.attachments = [deseralize(Attachment,
                                       attach) for attach in attachments]
        self.exchangeRateQuoteId = exchangeRateQuoteId
        self.dueDate = dueDate
