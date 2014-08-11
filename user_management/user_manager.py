from user_management.models import User

__author__ = 'SOROOSH'


class CaptchaException(Exception):
    pass


def _validate_captcha(user_input, captcha):
    if user_input.strip().lower() == captcha.strip().lower():
        return
    raise CaptchaException()


def register_user(user, input_captcha, session):
    _validate_captcha(input_captcha, session['captcha'])
    try:
        user.save()
    except Exception as e:
        print e


def authenticate(username,password):
    try:
        user = User.objects.get(username=username)
        if user.is_pass_correct(password):
            return user
        return None
    except Exception as e:
        print e
        return None

