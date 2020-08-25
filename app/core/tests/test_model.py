from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_sucessful(self):

        email = "mukeshbhatt18@gmail.com"
        password = "mukesh18"

        user = get_user_model().objects.create_user(
            email = email, 
            password = password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_normalized_email(self):
        email = 'mukeshbhatt@GMAIL.COM'
        password = 'mukesh123'

        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_user_cannot_create_without_email(self):
        email = None
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, password='mukesh123')
