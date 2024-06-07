from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')
        self.me_url = reverse('me')
        self.email = 'test@test.com'
        self.password = '123'
        self.access_token = None

    def test_signup(self):
        # 测试用户注册
        data = {'email': self.email, 'password': self.password}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signin_and_get_access_token(self):
        # 测试登录并且获取登录令牌
        self.test_signup()
        data = {'email': self.email, 'password': self.password}
        response = self.client.post(self.signin_url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.json().get('access')

    def test_get_me(self):
        # 测试根据令牌获取个人信息
        self.test_signin_and_get_access_token()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.get(self.me_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], self.email)
