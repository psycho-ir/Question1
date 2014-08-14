__author__ = 'soroosh'


class CaptchaException(Exception):
    pass


class UserAlreadyExistException(Exception):
    pass


class UserInActiveException(Exception):
    pass


class UserActivationExpired(Exception):
    pass
