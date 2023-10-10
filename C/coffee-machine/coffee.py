import art
import data
import os

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(coffee):
    if coffee=='espresso' and data.MENU[coffee]["ingredients"]["water"]<=resources["water"] and data.MENU[coffee]["ingredients"]["coffee"]<=resources["coffee"]:
        return True
    elif coffee!='espresso' and data.MENU[coffee]["ingredients"]["water"]<=resources["water"] and data.MENU[coffee]["ingredients"]["coffee"]<=resources["coffee"] and data.MENU[coffee]["ingredients"]["milk"]<=resources["milk"]:
        return True
    else:
        return False

def print_resources():
    print(f"Coffee: {resources['coffee']}")
    print(f"Milk: {resources['milk']}")
    print(f"Water: {resources['water']}")

def make_coffee(coffee):
    resources["coffee"]=resources["coffee"]-data.MENU[coffee]["ingredients"]["coffee"]
    resources["water"]=resources["water"]-data.MENU[coffee]["ingredients"]["water"]
    if coffee!='espresso':
        resources["milk"]=resources["milk"]-data.MENU[coffee]["ingredients"]["milk"]
    print(f"Enjoy your {coffee} 🤗☕")
    print_resources()


def enough_money(coffee):
    price=data.MENU[coffee]['cost']
    print(f"Enter {price}$ ---")
    quarters=int(input("Enter the amounts of quarters(0.25$): "))
    dimes=int(input("Enter the amounts of dimes(0.1$): "))
    nickles=int(input("Enter the amounts of nickles(0.05$): "))
    pennies=int(input("Enter the amounts of pennies(0.01$): "))
    
    given=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    if given==price:
        return True
    elif given>price:
        print(f"You gave me more money 😐, take the extra {given-price}$")
        return True
    else:
        return False


def restart():
    os.system('cls||clear')
    print(art.logo)

def do_command(coffee):
    if not enough_money(coffee):
        print("Not enough money😥!!!")
    elif not enough_resources(coffee):
        print("Not enough Resources😥!!!")
    else:
        make_coffee(coffee=coffee)
        

restart()
command=''
while command!='off':
    command=input("What would you like😄 ? (espresso/latte/cappuccino):")
    if command=='off':
        break
    elif command=='espresso' or command=='latte' or command=='cappuccino': 
        do_command(coffee=command)
    else:
        print("Not a command I recognise 🤔")
    
    
# restart()