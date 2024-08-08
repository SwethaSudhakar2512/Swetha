
# Create your tests here.

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class InterestTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.client.login(username='user1', password='password123')

    def test_send_interest(self):
        url = '/api/interests/'
        data = {'receiver': self.user2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_accept_interest(self):
        # Additional tests for accepting/rejecting interests and messaging
        pass
