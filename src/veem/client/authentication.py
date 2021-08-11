import urllib.parse

from odooveem.constants import (
    Scope,
    CLIENT_CREDENTIALS_GRANT_TYPE,
    AUTHORIZATION_CODE_GRANT_TYPE,
    REFRESH_TOKEN_GRANT_TYPE
)
from odooveem.client.responses.token import TokenResponse

from odooveem.client.base import Base
from odooveem.utils.rest import VeemRestApi

class AuthenticationClient(Base):

    def __init__(self, config, **kwargs):

        self.config = config
        self.context = config.context
        self.client = VeemRestApi(self.config.url,
                                  self.context.session,
                                  dict(getTokenFromClientCredentials=(
                                        'post', 'oauth/token'),
                                       refreshToken=('post', 'oauth/token'),
                                       getTokenFromAuthorizationCode=(
                                       'post', 'oauth/token')))

    def getTokenFromClientCredentials(self, scope=Scope.All):
        """
            Get Access token using API Client Credential
        """
        response = self._response_handler(TokenResponse,
            self.client.getTokenFromClientCredentials(
            request_auth=(self.context.clientId, self.context.clientSecret),
            request_params=dict(grant_type=CLIENT_CREDENTIALS_GRANT_TYPE,
                                scope=scope)
        ))
        self.context.token = response
        return response

    def refreshToken(self, refreshToken):
        """
            Refresh Access token
        """
        response = self._response_handler(TokenResponse,
            self.client.refreshToken(
            request_auth=(self.context.clientId, self.context.clientSecret),
            request_params=dict(grant_type=REFRESH_TOKEN_GRANT_TYPE,
                                refresh_token=refreshToken)
        ))
        self.context.token = response
        return response

    def getTokenFromAuthorizationCode(self, scope=Scope.All):
        """
            Refresh Access token from authorization code
        """
        response = self.client.refreshToken(
            request_auth=(self.context.clientId, self.context.clientSecret),
            request_params=dict(grant_type=AUTHORIZATION_CODE_GRANT_TYPE,
                           code=self.context.authorizationCode,
                           redirect_uri=urllib.parse.quote(context.redirectUrl),
                           scope=scope))
        return response
