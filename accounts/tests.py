from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="albany",
            email="albany@ejemplo.com",
            password="test1234"
        )

        self.assertEqual(user.username, "albany")
        self.assertEqual(user.email, "albany@ejemplo.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="saul",
            email="saul@ejemplo.com",
            password="test123456"
        )

        self.assertEqual(user.username, "saul")
        self.assertEqual(user.email, "saul@ejemplo.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)