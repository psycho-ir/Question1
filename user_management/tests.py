from django.test import TestCase
from user_management.models import User
from user_management.user_manager import authenticate, CaptchaException, register_user, activate

password = 123456


def persis_test_user():
    user = User()
    user.username = 'soroosh'
    user.email = 'soroosh.sarabadani@gmail.com'
    user.set_password(password)
    user.save()
    return user


fake_session = {'captcha': 'captcha'}


class UserPersistantTest(TestCase):
    def setUp(self):
        self.user = persis_test_user()

    def test_user_should_save_with_hashed_pass(self):
        self.assertEqual(self.user.password, self.user._hash(password, self.user.username))

    def test_is_pass_correct_should_return_True_when_pass_is_correct(self):
        self.assertTrue(self.user.is_pass_correct(password))

    def test_is_pass_correct_should_return_False_when_pass_is_wrong(self):
        self.assertFalse(self.user.is_pass_correct(12345))


class UserActivationException(object):
    pass


class UserManagementTest(TestCase):
    def setUp(self):
        self.user = persis_test_user()
        self.user.active = True
        self.user.save()

    def test_authenticate_shoud_return_User(self):
        self.assertEqual(authenticate('soroosh', password).email, self.user.email)

    def test_authenticate_should_return_None(self):
        self.assertIsNone(authenticate('soroosh', 12345))

    def test_register_should_return_Exception(self):
        u = User()
        u.username = 'ali'
        u.set_password('123')
        u.email = 'ali@iran.ir'
        self.assertRaises(CaptchaException, register_user, u, 'captch', fake_session)

    def test_register_should_save_user(self):
        u = User()
        u.username = 'ali'
        u.set_password('123')
        u.email = 'ali@iran.ir'
        u.active = True
        register_user(u, 'captcha', fake_session)
        self.assertIsNotNone(authenticate('ali', '123'))

    def test_activate_should_raise_exception_if_user_is_active(self):
        self.user.activation_code = '111'
        self.user.save()
        self.assertRaises(Exception, activate,'111')