from oveem.models.base import Base
from oveem.models.account import Account


class AccountResponse(Base):
    def __init__(self,
                 id=None,
                 firstName=None,
                 lastName=None,
                 name=None,
                 email=None,
                 isoCountryCode=None,
                 isContact=None,
                 **kwargs):

        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.name = name
        self.email = email
        self.isoCountryCode = isoCountryCode
        self.isContact = isContact

    @property
    def convert(self):
        return Account(**self.json)
