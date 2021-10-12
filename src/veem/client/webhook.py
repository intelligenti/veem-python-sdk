from veem.client.responses.webhook import WebhookResponse

from veem.client.base import Base
from veem.utils.rest import VeemRestApi

class WebhookClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(create=('post', ''),
                                       delete=('delete', '/{webhookId}'),
                                       get=('get','')))

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
    
    def delete(self, webhookId):
        """
            delete a specific webhook by id

            @param request: webhook id
            @return Webhook that you just requested
            @throws VeemException If the provided paymentId is invalid, or
                                  if cancelling fails.
        """
        return self._response_handler(WebhookResponse,
                                 self.client.delete(
                                        uri_params=dict(webhookId=webhookId),
                                        access_token=self.context.token,
                                        api_route='webhooks')
                                    )


    def get(self, webhookId):
        """
            Get a specific webhook by id

            @param request: webhook id
            @return Payment that you just requested
            @throws VeemException If the provided paymentId is invalid, or
                                  if retriving fails.
        """
        return self._response_handler(WebhookResponse,
                                 self.client.get(
                                        uri_params=dict(webhookId=webhookId),
                                        access_token=self.context.token,
                                        api_route='webhooks')
                                    )
