from odooveem.client.responses.page import PageResponse
from odooveem.client.responses.account import AccountResponse

from odooveem.client.base import Base
from odooveem.utils.rest import VeemRestApi

class CustomerClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(list=('get', '')))

    def list(self, request):
        """
            Matching Veem customer email with provided email address

            @param request: an AccountRequest or stirng of email
            @return paginated Accounts that matches the search criteria.
        """
        email = getattr(request, 'email', str(request))
        return self._list_response_handler(PageResponse,
                                 AccountResponse,
                                 self.client.list(
                                            request_params=dict(email=email),
                                            access_token=self.context.token,
                                            api_route='customers')
                                        )
