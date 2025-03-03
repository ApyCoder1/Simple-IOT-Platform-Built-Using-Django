import firebase_admin
from firebase_admin import credentials, db
import time

# Load Firebase credentials (Replace with your file path)
cred = credentials.Certificate("app1/apycoder-6c4a1-7869b5cca046.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://apycoder-6c4a1-default-rtdb.firebaseio.com/"
})

# Firebase LED control function
def control_led(state):
    ref = db.reference("/led/state")
    ref.set(state)  # Set 1 for ON, 0 for OFF
    print(f"LED State updated to: {'ON' if state else 'OFF'}")

# Simple menu for controlling LED
while True:
    user_input = input("Enter 1 to turn ON LED, 0 to turn OFF, q to quit: ")
    
    if user_input == "1":
        control_led(1)
    elif user_input == "0":
        control_led(0)
    elif user_input.lower() == "q":
        print("Exiting...")
        break
    else:
        print("Invalid input! Please enter 1, 0, or q.")
