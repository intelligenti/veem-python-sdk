
from odooveem.configuration import ConfigLoader
from odooveem.client.payment import PaymentClient
from odooveem.client.requests.payment import PaymentRequest
from odooveem.client.authentication import AuthenticationClient

if __name__ == '__main__':

    # loading SDK configuration from your yaml file
    config = ConfigLoader(yaml_file='/path/to/your/configuration.yaml')
    # login to Veem server with client credentials
    AuthenticationClient(config).getTokenFromClientCredentials()
    # define an PaymentRequest
    request = PaymentRequest(payee=dict(type='Business',
                                email='username@yourbusiness.com',
                                firstName='Joe',
                                lastName='Doe',
                                businessName='Your Business Inc.',
                                countryCode='US',
                                phoneCountryCode='1',
                                phone='02222222222'),
                     amount=dict(number=50, currency='USD'))
    # create a Draft payment
    payment = PaymentClient(config).create(request)
    # send the Drafted payment
    payment = PaymentClient(config).send(payment.id)
