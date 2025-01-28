import colorama
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"{Fore.YELLOW}{Style.BRIGHT}Rock, Paper and Scissors")
# logic behind it
askAgain = 0
tutorial = str(input("Do you know the rules?(y/n) "))
while tutorial != 0:
    while tutorial == "n":
        print("* A Rock beats scissors by smashing them")
        print("* Scissors beats paper by cutting it")
        print("* Paper beats rock by covering it")
        askAgain = str(input("Did you understand?(y/n) "))
        while askAgain != "y":
          print("* A Rock beats scissors by smashing them")
          print("* Scissors beats paper by cutting it")
          print("* Paper beats rock by covering it")
          askAgain = str(input("Did you know the rules?(y/n) "))
          if askAgain == "y":
            print("Okay, now you are ready to play!")
            tutorial = 0
          else:
            askAgain = str(input("Do you know the rules?(y/n) "))
    if tutorial == "y":
        print("do you know???????")
        tutorial = str(input("Do you know the rules?(y/n) "))
    else:
        tutorial = str(input("Do you know the rules?(y/n) "))