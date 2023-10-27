from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.menu1 = Menu.objects.create(title="Pasta", price=11.99, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=14.99, inventory=50)
        self.url = reverse('menu-list')

    def login_as_test_user(self):
        self.client.login(username='testuser', password='testpassword')

    def test_getall(self):
        self.login_as_test_user()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)