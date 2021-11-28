# Day 14
# Date: 28 Nov 2021
# Coffee Machine 
logo = '''

 ██████  ██████  ███████ ███████ ███████ ███████     ███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
██      ██    ██ ██      ██      ██      ██          ████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██      ██    ██ █████   █████   █████   █████       ██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██      ██    ██ ██      ██      ██      ██          ██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
 ██████  ██████  ██      ██      ███████ ███████     ██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
                                                                                                             
'''
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def report():
    for item in resources:
        print(f"{item} : {resources[item]}")
    


def detail(user_input):
    if user_input == 1:
        book = menu["espresso"]["ingredients"]
        for item in book:
            print(f"{item} : {book[item]}")

    elif user_input == 2:
        book = menu["latte"]["ingredients"]
        for item in book:
            print(f"{item} : {book[item]}")

    else:
        book = menu["cappuccino"]["ingredients"]
        for item in book:
            print(f"{item} : {book[item]}")


def check(user_input):
    reso_check = True
    if user_input == 1:
        book = menu["espresso"]["ingredients"]
        for item in book:
            if book[item] >= resources[item]:
                print(f'Sorry there is not enough {item}.\nPlease select another drink.')
                reso_check = False
        if reso_check == True:
            coins(1)
            

    elif user_input == 2:
        book2 = menu["latte"]["ingredients"]
        for item in book2:
            if book2[item] >= resources[item]:
                print(f'Sorry there is not enough {item}.\nPlease select another drink.')
                reso_check = False
        if reso_check == True:
            coins(2)
            
    else:
        book3 = menu["cappuccino"]["ingredients"]
        for item in book3:
            if book3[item] >= resources[item]:
                print(f'Sorry there is not enough {item}.\nPlease select another drink.')
                reso_check = False
        if reso_check == True:
            coins(3)
           

def coins(user_input):
    # quarters = 0.25 dimes =0.10  nickles=0.05   pennies = 0.01
    quarter = int(input('How many quarters? :'))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))
    total = quarter*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f"Your total money is {total}.")

    trans = True
    if user_input == 1:
        e_cost = menu["espresso"]["cost"]
        print(f"The coffee price is ${e_cost}.")
        if e_cost > total:
            print("Sorry, not enough money. Money refunded.")
            trans = False
        else:
            change = e_cost - total
            change = change*-1
            print(f'Here is your ${change}.')
            print("Here is your coffee. Enjoy!")
            ing_change(1)
            

    elif user_input == 2:
        l_cost = menu["latte"]["cost"]
        print(f"The coffee price is ${l_cost}.")
        if l_cost > total:
            print("Sorry, not enough money. Money refunded.")
            trans = False
        else:
            change = l_cost - total
            change = change*-1
            print(f'Here is your ${change}.')
            print("Here is your coffee. Enjoy!")
            ing_change(2)
            
    
    else :
        c_cost = menu["cappuccino"]["cost"]
        print(f"The coffee price is ${c_cost}.")
        if c_cost > total:
            print("Sorry, not enough money. Money refunded.")
            trans = False
        else:
            change = c_cost - total
            change = change*-1
            print(f'Here is your ${change}.')
            print("Here is your coffee. Enjoy!")
            ing_change(3)
            


def ing_change(user_input):
    if user_input == 1:
        water_change = resources["water"] - (menu["espresso"]["ingredients"]["water"])
        resources["water"] = int(water_change)
        coffee_change = resources["coffee"] - (menu["espresso"]["ingredients"]["coffee"])
        resources["coffee"] = int(coffee_change)

    elif user_input == 2:
        water_change = resources["water"] - (menu["latte"]["ingredients"]["water"])
        resources["water"] = int(water_change)
        coffee_change = resources["coffee"] - (menu["latte"]["ingredients"]["coffee"])
        resources["coffee"] = int(coffee_change)
        milk_change = resources["milk"] - (menu["latte"]["ingredients"]["milk"])
        resources["milk"] = int(milk_change)
        
    else:
        water_change = resources["water"] - (menu["cappuccino"]["ingredients"]["water"])
        resources["water"] = int(water_change)
        coffee_change = resources["coffee"] - (menu["cappuccino"]["ingredients"]["coffee"])
        resources["coffee"] = int(coffee_change)
        milk_change = resources["milk"] - (menu["cappuccino"]["ingredients"]["milk"])
        resources["milk"] = int(milk_change)
        



print(logo)
print("This is coffee making machine.\nFollow the instructions to get your favourite coffee.\nThe command for user are described in the process itslef.\nThe coffee machine owner can shut the machine by entering 'off' and check the status by entering'report'. ")

should_continue = True
while should_continue:
    print("\nWhat would you like?\nPress 1 for espresso\nPress 2 for latte\nPress 3 for cappuccino\n")
    user_input = input()

    if user_input == 'off':
        should_continue = False
        print("Shutting down..")

    elif user_input== "1":
        print("Your selected coffee is Espresso.")
        detail(1)
        check(1)
        

    elif user_input == "2":
        print("Your selected coffee is Latte.")
        detail(2)
        check(2)

    elif user_input == "3":
        print("Your selected coffee is Cappuccino.")
        detail(3)
        check(3)

    elif user_input == 'report':
        print("Reporting...")
        report()

    else :
        print("Invalid command!\nTry again.")

