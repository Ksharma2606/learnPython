import random

print("")
playerchoice = input("Enter .... \n1 for rock \n2 for paper \n3 for scissors \n")

player = int(playerchoice)
computerchoice = random.choice("123")
print("Computer chose", computerchoice)


if player == int(computerchoice):
    print("It's a tie")

elif player == 1 and computerchoice == "2":
    print("Computer wins")

elif player == 1 and computerchoice == "3":
    print("Player wins")

elif player == 2 and computerchoice == "1":
    print("Player wins")

elif player == 2 and computerchoice == "3":
    print("Computer wins")

elif player == 3 and computerchoice == "1":
    print("Computer wins")

elif player == 3 and computerchoice == "2":
    print("Player wins")



