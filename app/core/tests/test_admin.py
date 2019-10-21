from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        # create a test client
        self.client = Client()
        # create an admin user
        self.admin_user = get_user_model().objects.create_super_user(
            email='admin@flowfelis.com',
            password='foo'
        )
        # log in admin user
        self.client.force_login(self.admin_user)
        # create a regular user
        self.user = get_user_model().objects.create_user(
            email='test@flowfelis.com',
            password='foo',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Users are listed on admin page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """User change page renders successfully"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        """User add works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
