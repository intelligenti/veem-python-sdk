from veem.models.base import Base
from veem.models.exchange_rate import ExchangeRate

class WebhookResponse(Base):
    def __init__(self,
                 event=None,
                 callbackURL=None,
                 **kwargs):

        self.event = event
        self.callbackURL = callbackURL

    # @property
    # def convert(self):
    #     return ExchangeRate(hashId=self.id, **self.json)
