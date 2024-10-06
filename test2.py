from django.test import TestCase, RequestFactory
from django.core import signing
from django.http import JsonResponse
from rest_framework import status
from unittest.mock import patch

# Assuming 'models' refers to your Django models file
from . import models  # Replace with the actual path to your models

# Replace with your actual view class
class MyView(PagePermCheckMixin, TestCase.View):  # Example view using the mixin
    def get(self, request, *args, **kwargs):
        return JsonResponse({'detail': 'Success'})


class PagePermCheckMixinTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = models.User.objects.create(username="testuser")
        self.project = models.Project.objects.create(name="Test Project", user=self.user)
        self.page = models.Page.objects.create(title="Test Page", project=self.project)
        self.view = MyView.as_view()

    def test_missing_token(self):
        request = self.factory.get('/test/')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'detail': 'Missing token'})

    def test_no_page_id(self):
        auth_code = signing.dumps({"user_id": self.user.id})
        request = self.factory.get('/test/', HTTP_COOKIE=f'pd_auth_code={auth_code}')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'detail': 'No page_id provided.'})

    def test_no_permission(self):
        auth_code = signing.dumps({"user_id": self.user.id})
        request = self.factory.get(f'/test/{self.page.id+1}/', HTTP_COOKIE=f'pd_auth_code={auth_code}')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'detail': 'You haven\'t provided the correct credentials to access this.'})

    def test_valid_permission(self):
        auth_code = signing.dumps({"user_id": self.user.id})
        request = self.factory.get(f'/test/{self.page.id}/', HTTP_COOKIE=f'pd_auth_code={auth_code}')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'detail': 'Success'})

    @patch('app.models.Page.objects.filter')  # Replace 'app' with your app name
    def test_database_error(self, mock_filter):
        mock_filter.side_effect = Exception("Database error")
        auth_code = signing.dumps({"user_id": self.user.id})
        request = self.factory.get(f'/test/{self.page.id}/', HTTP_COOKIE=f'pd_auth_code={auth_code}')
        with self.assertRaises(Exception) as context:
            self.view(request)
        self.assertEqual(str(context.exception), "Database error")
