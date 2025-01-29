import colorama, time
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"-->{Fore.YELLOW}{Style.BRIGHT}Rock, Paper and Scissors{Style.RESET_ALL}<--")
tutorial = str(input("$ Do you know the rules?(y/n) "))
tutorial1 = 0
rules = {
   "Rule 1" : f"A {Fore.YELLOW}{Style.BRIGHT}Rock beats scissors{Style.RESET_ALL} by smashing them",
   "Rule 2" : f"{Fore.YELLOW}{Style.BRIGHT}Scissors beats paper{Style.RESET_ALL} by cutting it",
   "Rule 3" : f"{Fore.YELLOW}{Style.BRIGHT}Paper beats rock{Style.RESET_ALL} by covering it",
}
while tutorial != 0:
    if tutorial != "y" and tutorial != "n":
        tutorial = str(input("$ Do you know the rules?(y/n) "))
    if tutorial == "n":
        for value in rules.values():
            print(f"| {value} |")
            time.sleep(0.5)
        tutorial1 = str(input("$ Did you understand the rules?(y/n) "))
        while tutorial1 != "y" and tutorial1 != "n":
          tutorial1 = str(input("$ Did you understand the rules?(y/n) "))
        if tutorial1 == "y":
            tutorial = "y"
        elif tutorial1 == "n":
          print("Okay, I'll repeat it for you")
          time.sleep(0.5)
          tutorial = "n"
    if tutorial == "y":
        print("Okay, let's play")
        exit()