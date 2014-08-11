__author__ = 'SOROOSH'


class CaptchaException(Exception):
    pass


def _validate_captcha(user_input, captcha):
    if user_input.strip().lower() == captcha.strip().lower():
        pass
    raise CaptchaException()


def register_user(user, input_captcha, session):
    _validate_captcha(input_captcha, session['captcha'])
    try:
        user.save()
    except Exception as e:
        print e

