import colorama, time
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"{Fore.YELLOW}{Style.BRIGHT}Rock, Paper and Scissors")
tutorial = str(input("Do you know the rules?(y/n) "))
rules = {
   "Rule 1" : "A Rock beats scissors by smashing them",
   "Rule 2" : "Scissors beats paper by cutting it",
   "Rule 3" : "Paper beats rock by covering it",
}
while tutorial != 0:
    