from veem.models.base import Base
from veem.models.exchange_rate import ExchangeRate

class WebhookResponse(Base):
    def __init__(self,
                 id=None,
                 event=None,
                 callbackURL=None,
                 status=None,
                 **kwargs):

        self.id = id
        self.event = event
        self.callbackURL = callbackURL
        self.status = status