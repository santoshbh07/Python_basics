name = input("Enter your name: ")
bid_price = int(input("Enter your bid price: $"))
other_users = input("Other users? (yes/no): ")

secret_auction = {}
secret_auction[name] = bid_price

while other_users=="yes":
    print("\n"*500)
    other_user = input("Enter other user's name: ")
    other_bid_price = int(input("Enter other user's bid price: $"))
    secret_auction[other_user] = other_bid_price
    other_users = input("Other users? (yes/no): ")

print(secret_auction)
secret_auction_bids = []

for user, bid in secret_auction.items():
    secret_auction_bids.append(bid)

for user in secret_auction:
    if secret_auction[user] == max(secret_auction_bids):
        print(f"The winner is {user} with a bid amount of ${max(secret_auction_bids)}")