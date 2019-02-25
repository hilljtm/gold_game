import time
import secrets

#setup
yes_no = ["yes", "no"]
directions = ["left", "right"]

# Introduction
name = input("What is your name?\n")
print("Hello, " + name + ". Lets gamble!")
time.sleep(1)
print("Buffett preaches value investing but that's boring.")

time.sleep(2)
print("Forget using a broker, lets set up our own account")


response = ""
while response not in yes_no:
    response = input("Would you like to set up an account? \nyes or no\n")
    if response == "yes":
        print("I always knew you were a gambler.\n")
    elif response == "no":
        print(
            "Scared money dont make no money,"
            + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Next part of game
response = ""
while response not in directions:
    print("On your left, you see a bank.")
    print("On your right, there is Bitcoin ATM.")
    response = input("Which way ?\n right or left \n")
    if response == "left":
        print("Enjoy inflation!,and centralization " + name + ".")
        quit()
    elif response == "right":
        print("Good choice. Let's buy some Bitcoin\n")
        break
    else:
        print("It's not that difficult to read the rules, try again champ.\n")
    
print("Now that you've got some Bitcoin let's go gamble")
print("One thing to note, The saying goes 'Not your keys, not your bitcoin.'")
time.sleep(1)
print(secrets.token_hex(16))
time.sleep(1)
print("You should probably write this down, don't tell anybody your private key!")
print("Private keys are what allow's you to spend your Bitcoin!")

#def bank(self, boss, name):
    