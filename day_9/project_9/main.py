from art import logo

print("Welcome to the secret auction program.")
print(logo)

bid_info = {
   
}

response = "yes"

while response == "yes":
    name = input("What is your name?\n")
    bid_info[name] = ''

    bid_amount = input("What is your bid?\n")
    bid_info[name] = bid_amount

    response = input("Are there any other bidder? Type 'yes' or 'no'\n").lower()

    if response == "yes":
        print("\n" * 100)

max_bid_amount = 0
winner_name = ''

for name, amount in bid_info.items():
    if int(amount) > int(max_bid_amount):
        max_bid_amount = amount
        winner_name = name

print(f"{winner_name} has won this competition with highest {max_bid_amount}$ bid amount")



