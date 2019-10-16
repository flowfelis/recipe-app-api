from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email successful"""
        email = 'test@flowfelis.com'
        password = 'foo'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalization(self):
        """Email is lowercase when creating new user"""
        email = 'test@FLOWfelis.com'

        user = get_user_model().objects.create_user(
            email=email,
            password='foo'
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_with_blank_email(self):
        """Creating user with blank email raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='foo'
            )

    def test_create_super_user(self):
        """Create a super user"""
        user = get_user_model().objects.create_super_user(
            'ali@flowfelis.com',
            'foo'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
