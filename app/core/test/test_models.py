from audioop import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""

        email = "bizu@gmail.com"
        password = 'Bizu123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = "bizu@gmail.com"
        user = get_user_model().objects.create_user(email,'Bizu123')

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """test creating a new user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Bizu123')

    def create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'bizu@gmail.com',
            'Bizu123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
