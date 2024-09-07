from art import logo

print(logo)


def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        current_bid = bids[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = bidder

    print(f"The winner is {winner} with a bid of €{highest_bid}")


bids = {}

while True:
    name = input("What is your name? ")
    try:
        bid = float(input("What is your bid? €"))
    except ValueError:
        print("A bid can only contain numbers! Try again!")
        continue

    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'. ").lower()

    if should_continue == "yes":
        print("\n" * 100)
        continue

    elif should_continue == "no":
        find_highest_bid(bids)
        break
    else:
        print("Invalid choice!")
        break
