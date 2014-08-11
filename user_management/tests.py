from django.test import TestCase
from user_management.models import User
from user_management.user_manager import authenticate

password = 123456


def persis_test_user():
    user = User()
    user.username = 'soroosh'
    user.email = 'soroosh.sarabadani@gmail.com'
    user.set_password(password)
    user.save()
    return user


class UserPersistantTest(TestCase):
    def setUp(self):
        self.user = persis_test_user()

    def test_user_should_save_with_hashed_pass(self):
        self.assertEqual(self.user.password, self.user._hash(password, self.user.username))

    def test_is_pass_correct_should_return_True_when_pass_is_correct(self):
        self.assertTrue(self.user.is_pass_correct(password))

    def test_is_pass_correct_should_return_False_when_pass_is_wrong(self):
        self.assertFalse(self.user.is_pass_correct(12345))


class UserManagementTest(TestCase):
    def setUp(self):
        self.user = persis_test_user()

    def test_authenticate_shoud_return_True(self):
        self.assertEqual(authenticate('soroosh', password).email,self.user.email)