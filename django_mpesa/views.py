from django.shortcuts import render,redirect
from .forms import InputForm
import requests
 
# Create your views here.
def home(request):
    '''
    view function for landing page
    '''
    form = InputForm()
    return render(request, 'home.html', {"form":form })


def mpesa(request):
    name = request.POST.get('name')
    print(name)
    phone_number = request.POST.get('phone_number')
    print(phone_number)

    access_token = "IEwGqES8rZhvqqgvrMnfIvBkjBrr"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgxMjE5MTA0MTEw",
        "Timestamp": "20181219104110",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254728322478",
        "PartyB": "174379",
        "PhoneNumber": "%s" % phone_number,
        "CallBackURL": "http://daraja1.000webhostapp.com/confirmation.php",
        "AccountReference": "refref",
        "TransactionDesc": "test"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

    return redirect(home)