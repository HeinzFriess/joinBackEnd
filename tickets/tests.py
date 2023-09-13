from django.test import TestCase,Client
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token

# Create your tests here.

class FirstTest(TestCase):

    def setUp(self):
        self.user = User(username='test_user')
        password='#sseirF11dj'
        self.user.set_password(password)
        self.user = User.objects.create_user('test_user', )
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client = Client() 
        self.client.login(username='test_user', password='#sseirF11dj')

    def testOne(self):
        
        response = self.client.get('/ticket/', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(response, user=self.user) 
        self.assertEqual(response.status_code, 200)