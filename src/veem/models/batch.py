
from odooveem.models.base import Base
from odooveem.models.batch_item import BatchItem

from odooveem.utils import deseralize
from odooveem.constants import BatchStatus

class Batch(Base):
    def __init__(self,
                 id=None,
                 batchId=None,
                 status=None,
                 hasErrors=None,
                 processedItems=None,
                 totalItems=None,
                 batchItems=[],
                 **kwargs):

        self._validate_constants(BatchStatus, status)

        self.id = id or batchId
        self.batchId = id or batchId
        self.status = status
        self.hasErrors = hasErrors
        self.processedItems = processedItems
        self.totalItems = totalItems
        self.batchItems = [deseralize(BatchItem, b) for b in batchItems]
