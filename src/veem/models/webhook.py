
from veem.models.base import Base

class Webhook(Base):
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
