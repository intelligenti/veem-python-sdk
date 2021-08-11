
from oveem.models.base import Base
from oveem.models.address import Address

from oveem.utils import deseralize
from oveem.constants import ApprovalStatus

class BankAccount(Base):
    def __init__(self,
                 status=None,
                 email=None,
                 firstName=None,
                 lastName=None,
                 middleName=None,
                 **kwargs):

        self._validate_currency_code(currencyCode)
        self._validate_country_code(isoCountryCode)
        self._validate_constants(ApprovalStatus, status)

        self.routingNumber = routingNumber
        self.bankName = bankName
        self.bankAccountNumber = bankAccountNumber
        self.currencyCode = currencyCode
        self.isoCountryCode = isoCountryCode
        self.iban = iban
        self.swiftBic = swiftBic
        self.beneficiaryName = beneficiaryName
        self.bsbBankCode = bsbBankCode
        self.branchCode = branchCode
        self.transitCode = transitCode
        self.bankInstitutionNumber = bankInstitutionNumber
        self.bankIfscBranchCode = bankIfscBranchCode
        self.sortCode = sortCode
        self.bankCode = bankCode
        self.clabe = clabe
        self.bankCnaps = bankCnaps
        self.bankAddress = deseralize(Address, bankAddress)
