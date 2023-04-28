print("Hello World")

import random

destination_list = ["Austin, Texas", "Portland, Oregon", "San Diego, California", "Laguna Beach, California", "Ashville, North Carolina", "Charleston, South Carolina", "Yellowstone National Park-Wyoming Entrance"]

def location_picker(list):
    random_location = random.choice(list)
    return random_location

def destination_location_picker():
    user_picked = False
    while user_picked == False:
        random_location = location_picker(destination_list)
        print(f"We have randomly selected {random_location} for your destination. Would you like this added to your itinerary?")
        user_choice = input("Enter 'yes' to keep this destination or 'no' to see a new random city...")
        if user_choice == "yes":
            print(f"{random_location} was added to your intinerary")
            user_picked = True
            return random_location
        elif user_choice == "no":
            print("Let's try a different option. How do you like this?")

destination_result = destination_location_picker()
print(f"We selected {destination_result} for your trip! Have Fun!")

import random

mode_of_transportation_list = ["Bicycle", "Car", "Tour Bus", "Private Plane", "Electric Scooter", "Uber", "Motorcycle"]

def transportation_picker(list):
    random_transport = random.choice(list)
    return random_transport

def mode_of_transportation_picker():
    user_picked = False
    while user_picked == False:
        random_transport = transportation_picker(mode_of_transportation_list)
        print(f"We have randomly selected {random_transport} for your mode of transportation. Would you like this added to your itinerary?")
        user_choice = input("Enter 'yes' to keep this modeo of transportation or 'no' to see a new random option...")
        if user_choice == "yes":
            print(f"Great! {random_transport} was added to your intinerary.")
            user_picked = True
            return random_transport
        elif user_choice == "no":
            print("Here is another random selection for you.")

transportation_result = mode_of_transportation_picker()
print(f"We selected {transportation_result} for your trip. Enjoy your mode of transportation!")
