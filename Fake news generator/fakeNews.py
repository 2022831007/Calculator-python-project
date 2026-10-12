import random
subjects = [
    "Habib Wahid",
    "Mustafiz",
    "Nirmala debi",
    "A Dhakaia Cat",
    "Prime minister Imran Khan",
    "A Group of Monkeys",
    "Auto Rickshaw Driver from Dhaka"
]

actions = [
    "Launches",
    "cancels",
    "dances with",
    "eats",
    "Declares war on",
    "orders",
    "celebrates"
]
places_of_things = [
    "at lal bagh kella",
    "in dhaka local train",
    "a plate of samosa",
    "inside parliament",
    "at sylhet cha bagan",
    "during BPL Match",
    "at zinda park"

]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_of_thing = random.choice(places_of_things)
    
    headline = f"Breaking News🔥 : { subject} { action} { place_of_thing} "
    print("\n" + headline)

    user_input = input("Do you want  another headline? (yes/no)").strip() # remove extra space for using strip()
    if user_input == "no":
        break

print("\n Thanks for  using the Fake News headline Generator.Have a Fun Day 😊")
