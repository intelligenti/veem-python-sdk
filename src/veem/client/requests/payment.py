
from .amount import AmountRequest
from .account import AccountRequest
from .attachment import AttachmentRequest

from odooveem.models.base import Base

from odooveem.utils import deseralize

class PaymentRequest(Base):
    def __init__(self,
                 batchItemId=None,
                 exchangeRateQuoteId=None,
                 payee=None,
                 amount=None,
                 notes=None,
                 externalInvoiceRefId=None,
                 ccEmails=[],
                 purposeOfPayment=None,
                 attachments=[],
                 approveAutomatically=False,
                 **kwargs):

        self.batchItemId = batchItemId
        self.exchangeRateQuoteId = exchangeRateQuoteId
        self.payee = deseralize(AccountRequest, payee).json
        self.amount = deseralize(AmountRequest, amount).json
        self.notes = notes
        self.externalInvoiceRefId = externalInvoiceRefId
        self.ccEmails = ccEmails
        self.purposeOfPayment = purposeOfPayment
        self.attachments = [deseralize(AttachmentRequest,
                                       attach).json for attach in attachments]
        self.approveAutomatically = approveAutomatically
