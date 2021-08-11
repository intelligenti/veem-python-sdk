from oveem.models.base import Base

class AttachmentResponse(Base):
    def __init__(self,
                 type=None,
                 name=None,
                 referenceId=None,
                 **kwargs):

        self.type = type
        self.name = name
        self.referenceId = referenceId
