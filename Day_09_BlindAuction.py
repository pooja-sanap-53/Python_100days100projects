# Day 09
# Date: 23 Nov 2021
# Blind Auction

from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print('''Blind Auction is a type of auction process in which all bidders place offers simultaneously to buy or sell without seeing the current bids and offers.

Here you can also bid and try to win the auction!
All you have to do is to follow the instructions.
And later on pass the device to other bidders(if any.)
''')

enteries = {}
should_continue = True

def highest_bidder(bidding_records):
    highest_bid = 0
    winner= ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner =  bidder
    print(f"Congratulations!! The highest bid is of ${highest_bid} by {winner}!")
    
while should_continue:
    name = input("\nEnter your name:")
    bid_price = float(input("Enter your bid price: $"))

    enteries[name] = bid_price

    print(enteries)
    end = input("Are there any bidders left? \nType 'yes' if they are , and 'no' if there are none.\n").lower()
    if end == "yes":
        print("\nPlease handover to next bidder.")
        clear()
    elif end =="no":
        should_continue = False
        highest_bidder(enteries)
        print("\nThankyou!")
        
    else :
        print("Invalid input!\n Try again!")

