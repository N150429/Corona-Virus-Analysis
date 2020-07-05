# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:40:11 2020

@author: RockyRaju
"""

from twilio.rest import Client 

account_sid = 'AC413f25369c98cf2a6bc383e23747e847' 
auth_token = '91a037578c8192c976e8458a3cc9f03c' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hello darling, sweetheart',      
                              to='whatsapp:+919553649202' 
                          ) 
 
print(message.sid)