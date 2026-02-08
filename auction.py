from os import system

logo = r'''
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

#ures dictionary létrehozása, program inic és while feltétel deklarálása

print(f"{logo}\n")
print("<><><><><><>     Welcome to the auction game!    <><><><><><>")

biders_bid = {}
bidding = True

#

while(bidding):

  print("Who is the bider?: ")
  key_name = input()
  value = int(input("What is your bid?: $"))

  biders_bid[key_name] = value 
  print("Are there any bidder left?(y/n): ")
  choice = input()
  if choice == "n":
     bidding = False
  system("clear||cls")
bigest_bid = 0

for key in biders_bid:
    if biders_bid[key] > bigest_bid:
        bigest_bid = biders_bid[key]
    if biders_bid[key] == bigest_bid:
        bigest_bidder = key

print(f"And the biggest bid is: ${bigest_bid} from {bigest_bidder}")
