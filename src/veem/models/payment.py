from oveem.models.base import Base
from oveem.models.amount import Amount
from oveem.models.account import Account
from oveem.models.attachment import Attachment
from oveem.models.exchange_rate import ExchangeRate
from oveem.models.payment_approval import PaymentApproval
from oveem.models.push_payment_info import PushPaymentInfo

from oveem.utils import deseralize
from oveem.constants import PaymentStatus

class Payment(Base):
    def __init__(self,
                 id=None,
                 status=None,
                 exchangeRate=None,
                 timeCreated=None,
                 claimLink=None,
                 pushPaymentInfo=None,
                 paymentApproval=None,
                 batchItemId=None,
                 payee=None,
                 payer=None,
                 clientId=None,
                 amount=None,
                 notes=None,
                 externalInvoiceRefId=None,
                 ccEmails=[],
                 purposeOfPayment=None,
                 attachments=[],
                 exchangeRateQuoteId=None,
                 **kwargs):

        self._validate_constants(PaymentStatus, status)

        self.id = id
        self.status = status
        self.exchangeRate = deseralize(ExchangeRate, exchangeRate)
        self.timeCreated = timeCreated
        self.claimLink = claimLink
        self.pushPaymentInfo = deseralize(PushPaymentInfo, pushPaymentInfo)
        self.paymentApproval = deseralize(PaymentApproval, paymentApproval)
        self.batchItemId = batchItemId
        self.payee = deseralize(Account, payee)
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

    def _generate_request(self, approveAutomatically=False):
        return PaymentRequest(
                     batchItemId=self.batchItemId,
                     exchangeRateQuoteId=self.exchangeRateQuoteId,
                     payee=self.payee,
                     amount=self.amount,
                     notes=self.notes,
                     externalInvoiceRefId=self.externalInvoiceRefId,
                     ccEmails=self.ccEmails,
                     purposeOfPayment=self.purposeOfPayment,
                     attachments=self.attachments,
                     approveAutomatically=approveAutomatically,
                )
