import hashlib
from uuid import uuid4
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=250)
    register_date = models.DateTimeField(auto_now_add=True)

    def _hash(self, plain_text, salt):
        return hashlib.sha512(str(plain_text) + str(salt)).hexdigest()


    def set_password(self, plain_pass):
        self.password = self._hash(plain_pass, self.username)

    def is_pass_correct(self, password):
        hashed_password = self._hash(password, self.username)
        if self.password == hashed_password:
            return True
        return False

    def generate_activation_code(self):
        self.activation_code = uuid4().hex

    def __unicode__(self):
        return 'username:%s , Email:%s , Password: Hmmmmm, i forgot it sorry man ;)' % (self.username, self.email)
