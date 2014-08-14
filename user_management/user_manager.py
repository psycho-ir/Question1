__author__ = 'SOROOSH'
from datetime import datetime, timedelta
from user_management.exceptions import CaptchaException, UserAlreadyExistException, UserActivationExpired, UserInActiveException
from user_management.mail import send_mail
from user_management.models import User



def _validate_captcha(user_input, captcha):
    if user_input.strip().lower() == captcha.strip().lower():
        return
    raise CaptchaException()


def register_user(user, input_captcha, session):
    _validate_captcha(input_captcha, session['captcha'])
    if User.objects.filter(username=user.username).exists():
        raise UserAlreadyExistException()
    user.generate_activation_code()
    user.full_clean()
    user.save()
    send_mail(user.email, 'You activation code is: %s' % user.activation_code)

def authenticate(username, password):
    try:
        user = User.objects.get(username=username)
        if user.is_pass_correct(password):
            if user.active:
                return user
            else:
                raise UserInActiveException("User is inactive. First activate your user with sent activation code.")
        return None
    except UserInActiveException as e:
        raise e
    except Exception as e:
        print e
        return None


def activate(code):
    user = User.objects.get(activation_code=code)
    if user.active:
        raise Exception("User has been activated before.")
    threshold_date = datetime.now() - timedelta(days=1)
    if threshold_date > user.register_date:
        raise UserActivationExpired('User Activation expired :)')
    user.active = True
    user.save()