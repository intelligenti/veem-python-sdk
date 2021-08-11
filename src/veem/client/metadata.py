from oveem.client.responses.page import PageResponse
from oveem.client.responses.metadata import CountryInfoResponse

from oveem.client.base import Base
from oveem.utils.rest import VeemRestApi
from oveem import __API_VERSION__ as API_VERSION

class MetadataClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.url = "veem/public/v{}/country-currency-map".format(API_VERSION)
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(getCountryCurrencyMap=('get',self.url)))

    def getCountryCurrencyMap(self):
        """
            Get all supported country and currency map
        """
        return self._list_response_handler(PageResponse,
                                           CountryInfoResponse,
                                           self.client.getCountryCurrencyMap())
