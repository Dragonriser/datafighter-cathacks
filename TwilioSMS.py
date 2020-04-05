from twilio.rest import Client
import re

def sendSMS(a, phoneNumber):
    
    account_sid = 'accountsid'
    auth_token = 'authtoken'
    client = Client(account_sid, auth_token)
    
    toNumber = str(phoneNumber)
    toNumber = re.sub('[^0-9]','', toNumber)
    toNumber = '+' + toNumber
    
    fromNumber = 'fromnumber'
    
    message = client.messages \
                  .create(body=a,
                      from_=fromNumber,
                      to=toNumber)
                  
#sendSMS("abc")                 
