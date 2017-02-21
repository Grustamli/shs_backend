from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()

request = factory.post('/phone-numbers/create', {'number': 0552104025}, format='json')

# Create your tests here.
