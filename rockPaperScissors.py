import colorama, time
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"-->{Fore.YELLOW}{Style.BRIGHT}Rock, Paper and Scissors{Style.RESET_ALL}<--")

understood = 0
rules = [
   f"A {Fore.YELLOW}{Style.BRIGHT}Rock beats scissors{Style.RESET_ALL} by smashing them",
   f"{Fore.YELLOW}{Style.BRIGHT}Scissors beats paper{Style.RESET_ALL} by cutting it",
   f"{Fore.YELLOW}{Style.BRIGHT}Paper beats rock{Style.RESET_ALL} by covering it"
]