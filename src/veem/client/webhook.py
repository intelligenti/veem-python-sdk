from veem.client.responses.webhook import WebhookResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi

class WebhookClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(create=('post', '/')))

    def create(self, request):
        """
            Create webhook for inbound and outbound payments.

            @param request: an WebhookRequest with event and callbackURL
            @return result from the server
        """
        return self._response_handler(
                        WebhookResponse,
                        self.client.create(access_token=self.context.token,
                                        api_route='webhooks',
                                        **request.json)
                            )
