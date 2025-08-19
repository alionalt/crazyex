import random
import time

# List of friends/exes with patience levels
contacts = {
    "Alex": 5,
    "Sam": 3,
    "Jordan": 4
}

messages = ["yooo", "fine shyt?", "lwk missed you :(", "you around?", "sup"]

def send_message(contact, patience):
    print(f"sending to {contact}...")
    time.sleep(1)
    msg = random.choice(messages)
    print(f"{contact} received: {msg}")
    
    # Random chance they reply
    if random.randint(1,10) > 7:
        print(f"{contact} replied!\n")
        return True
    else:
        print(f"{contact} ignored the message.\n")
        return False

# Main loop
for contact, patience in contacts.items():
    attempts = 0
    replied = False
    
    while not replied and attempts < patience:
        attempts += 1
        replied = send_message(contact, patience)
    
    if not replied:
        print(f"{contact} stopped replying.\n")
