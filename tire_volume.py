import math
import datetime

pi = math.pi
width = -1
asp_ratio = -1
diam = -1

print("\nHi, Welcome! This program computes the approximate volume of air inside a tire.\nFor that, can we know the... ")

while width < 0:
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    if width < 0:
        print("Please, enter a positive number.")
if width > -1:
    print(" ")

while asp_ratio < 0:
    asp_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    if asp_ratio < 0:
        print("Please, enter a positive number.")
if asp_ratio > -1:
    print(" ")

while diam < 0:
    diam = float(input("Enter the diameter of the wheel in inches (ex 15): "))
    if diam < 0:
        print("Please, enter a positive number.")
if diam > -1:
    print(" ")

volume = (pi * width * width * asp_ratio * (width * asp_ratio + 2540 * diam)) / 10000000

print(f"\nThe volume is {volume:.2f} milliliters cubic.\n")

# Find tire prices $ based on the entered dimensions.
tire_price = 0  

if 175 <= width <= 185 and 65 <= asp_ratio <= 75 and 14 <= diam <= 17:
    tire_price = 100
elif 195 <= width <= 205 and 55 <= asp_ratio <= 70 and 15 <= diam <= 18:
    tire_price = 120
elif 215 <= width <= 225 and 50 <= asp_ratio <= 60 and 16 <= diam <= 19:
    tire_price = 140
else:
    tire_price = 0 

# Print the tire price
if tire_price > 0:
    print(f"Tire Price: ${tire_price}")

# Ask the user if they want to buy tires
buy_tires = input("Do you want to buy tires with these dimensions (yes/no)? ").lower()

if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")

    
    # Getting the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Opening the text file for appending and write the data
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {asp_ratio}, {diam}, {volume:.2f}, {phone_number}\n")