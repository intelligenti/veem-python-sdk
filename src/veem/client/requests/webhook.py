from veem.models.base import Base

class WebhookRequest(Base):
    def __init__(self,
                 event=None,
                 callbackURL=None,
                 **kwargs):

        self.event = event
        self.callbackURL = callbackURL
