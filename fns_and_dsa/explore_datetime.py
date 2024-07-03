from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S") 

print("Current date and time: ", display_current_datetime())

Newdays = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = display_current_datetime() + timedelta(days=Newdays)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print("Future date: ", calculate_future_date()) 

