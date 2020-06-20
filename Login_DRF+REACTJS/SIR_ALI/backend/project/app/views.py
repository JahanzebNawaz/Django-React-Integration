from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import PasswordReset
from django.core.mail import EmailMessage, send_mail
from project.settings import EMAIL_HOST_USER

import random
import json
# Create your views here.


def password_reset_email( email_to, reset_code):
        '''
                Password Reset Email
        '''
        subject = 'Password Reset Email'
        text_message = ''' Your verification code is {}, click the link to reset password.
        	http://127.0.0.1:3000/password/update/
        '''.format(reset_code)

        mail = EmailMessage(subject, text_message, EMAIL_HOST_USER,
                        [email_to])
        mail.send()
        return True


class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer



@api_view(['POST'])
def password_reset(request):
        '''
                Password Reset View Function
        '''
        if request.method == 'POST':
                req_data = request.data
                # print(req_data['email'])
                
                check_user = User.objects.filter(email=req_data['email'])
                
                if check_user:
                        reset_code = ''.join(random.choice('1234567890') for _ in range(6))
                        print(reset_code)

                        userr = User.objects.get(email = req_data['email'])
                        print(userr.id)
                        user_id = User(id=userr.id)
                        # print(user_id)
                        database_entry = PasswordReset(user=user_id, code=reset_code )
                        database_entry.save()

                        # email sending
                        mail = password_reset_email(email_to=req_data['email'], reset_code=reset_code)

                        resp = {
                                'message': 'We have sent you an email for password reset.',
                                'status': 'Success'
                        }

                        return HttpResponse(json.dumps(resp))
                else:
                        resp = {
                                'message': 'No account found with this email',
                                'status': 'Error'
                        }
                        return HttpResponse(json.dumps(resp))



@api_view(['POST'])
def password_update(request):
        '''

        '''
        if request.method == 'POST':
                req_data = request.data
                # print(req_data['email'])
                email = req_data['email']
                code = req_data['code']
                password = req_data['password']
                
                check_user = User.objects.filter(email=email)
                if check_user:
                        userr = User.objects.get(email = email)
                        # print(userr.id)
                        user_id = User(id=userr.id)
                        # print(user_id)
                        check_reset_status = PasswordReset.objects.filter(user=user_id, code=code, status='Active').exists()

                        if check_reset_status:
                                row_data = PasswordReset.objects.get(user=user_id, code=code, status='Active')
                                row_data.status = 'Expired'
                                row_data.save()

                                # password update
                                userr.set_password(password)
                                userr.save()

                                resp = {
                                        'message': 'Password Updated.',
                                        'status': 'Success'
                                }
                                return HttpResponse(json.dumps(resp))

                        else:
                                resp = {
                                        'message': 'No Match found check email and verification code.',
                                        'status': 'Error'
                                }
                                return HttpResponse(json.dumps(resp))
                else:
                        resp = {
                                'message': 'No account found with this email',
                                'status': 'Error'
                        }
                        return HttpResponse(json.dumps(resp))
