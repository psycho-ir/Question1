from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


    def set_password(self, plain_pass):
        pass