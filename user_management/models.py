import hashlib
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)


    def _hash(self, plain_text, salt):
        return hashlib.sha512(str(plain_text) + str(salt)).hexdigest()


    def set_password(self, plain_pass):
        self.password = self._hash(plain_pass, self.username)

    def is_pass_correct(self, password):
        hashed_password = self._hash(password, self.username)
        if self.password == hashed_password:
            return True
        return False
