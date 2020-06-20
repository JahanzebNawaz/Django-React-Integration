from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class PasswordReset(models.Model):
        '''
                Database Table for password reset.
                Custom Token Codes for User Password Reset
        '''
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        code = models.CharField(max_length=20)
        status = models.CharField(max_length= 50, default='Active')

        date = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.user