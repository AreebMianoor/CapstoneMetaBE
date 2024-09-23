from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse  
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient 

class MenuViewTest(TestCase):

    def setUp(self):
        # Create a few Menu objects to use in tests
        self.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(title="Burger", price=120, inventory=50)

        # Create a user and generate a token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)

        # Set up the API client
        self.client = APIClient()  # Use APIClient instead of the default client

    def test_getall(self):
        # Include the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get(reverse('menu-items')) 
        self.assertEqual(response.status_code, 200)
        # Check if the correct number of items is returned
        self.assertEqual(len(response.data), 2)
        # Check if the serialized data equals the response content
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data
        self.assertEqual(response.data, serialized_data)

        # Check specific fields of the returned items
        self.assertEqual(response.data[0]['title'], 'IceCream')
        self.assertEqual(response.data[0]['price'], '80.00')  
        self.assertEqual(response.data[1]['title'], 'Burger')
        self.assertEqual(response.data[1]['price'], '120.00') 
