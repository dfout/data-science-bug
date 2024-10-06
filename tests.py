from django.test import TestCase, RequestFactory
from django.core import signing
from django.http import JsonResponse
from rest_framework import status
from unittest.mock import patch, MagicMock


# Assuming your models.py file contains the Page model
# Create a dummy Page model for testing if you don't have one already
class Page(MagicMock):
    objects = MagicMock()

    class DoesNotExist:
        pass


# Mock the models module
class MockModels:
    Page = Page


# Replace your actual import with this for testing
models = MockModels


class PagePermCheckMixinTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.mixin = PagePermCheckMixin()
        self.page_id = 1
        self.user_id = 1
        self.auth_code = signing.dumps({'user_id': self.user_id})

    def test_dispatch_missing_token(self):
        request = self.factory.get('/test/')
        response = self.mixin.dispatch(request, page_id=self.page_id)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'detail': 'Missing token'})

    def test_dispatch_no_page_id(self):
        request = self.factory.get('/test/', HTTP_COOKIE=f'pd_auth_code={self.auth_code}')
        response = self.mixin.dispatch(request)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'detail': 'No page_id provided.'})
    
    @patch.object(models.Page.objects, 'filter')
    def test_dispatch_no_permission(self, mock_filter):
        mock_filter.return_value.exists.return_value = False
        request = self.factory.get('/test/', HTTP_COOKIE=f'pd_auth_code={self.auth_code}', page_id=self.page_id)
        response = self.mixin.dispatch(request, page_id=self.page_id)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.json(),
            {'detail': 'You haven\'t provided the correct credentials to access this.'}
        )
        mock_filter.assert_called_once_with(id=self.page_id, project__user_id=self.user_id)
    
    @patch.object(models.Page.objects, 'filter')
    def test_dispatch_has_permission(self, mock_filter):
        mock_filter.return_value.exists.return_value = True
        
        class MockView:
            def dispatch(self, request, *args, **kwargs):
                return JsonResponse({'detail': 'Success'}, status=status.HTTP_200_OK)

        with patch('__main__.PagePermCheckMixin.__init__', return_value=None):
            self.mixin.__init__() # Need to re-initialize to avoid super().__init__() call during setup 
            self.mixin.dispatch = PagePermCheckMixin.dispatch.__get__(self.mixin, PagePermCheckMixin)
            request = self.factory.get('/test/', HTTP_COOKIE=f'pd_auth_code={self.auth_code}', page_id=self.page_id)
            
            # Mock the super().dispatch call
            with patch('__main__.super') as mock_super:
                mock_super_instance = mock_super.return_value
                mock_super_instance.dispatch.return_value = MockView().dispatch(request)

                response = self.mixin.dispatch(request, page_id=self.page_id)

                self.assertIsInstance(response, JsonResponse)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.json(), {'detail': 'Success'})
                mock_filter.assert_called_once_with(id=self.page_id, project__user_id=self.user_id)

