#!/usr/bin/python

from gpiozero import LED
from requests import get  
import json
import time                                                     
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("finalkey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Light Default 

ledBathroom = LED(17)   #red
ledKitchen = LED(22)    #green
ledBedroom = LED(27)    #yellow


doc_ref = db.collection('light').document('U5ecd214f1c2ed4ef31f14b313f09c843')
docs = doc_ref.get()
docs = docs.to_dict()
ledBathState = docs['bathroom']
ledKitchState = docs['kitchen']
ledBedState = docs['bedroom']

'''
ledBathState = True
ledKitchState = True
ledBedState = True
'''

# Light Default 


while True:
    
    try:
      ledBathState = docs['bathroom']
      ledKitchState = docs['kitchen']
      ledBedState = docs['bedroom']
      ledBathroom.value = ledBathState
      ledKitchen.value = ledKitchState
      ledBedroom.value = ledBedState
    
      print("Change!!")
      docs = doc_ref.get()
      docs = docs.to_dict()
      print("Done!!")
    except :
      print( "Device no register" )
     
    #ledBathState = input('Bathroom: ')
    #ledBathroom.value = ledBathState
    #ledKitchState = input('Kitchen: ')
    #ledKitchen.value = ledKitchState
    #ledBedState = input('Bedroom: ')
    #ledBedroom.value = ledBedState

