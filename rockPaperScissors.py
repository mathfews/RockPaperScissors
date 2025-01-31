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
def ask(text):
   while True:
    ask = input(text)
    if ask == "y":
      return True
    if ask == "n":
      return False
if ask("Do you want to know the rules?(y/n) "):
   while True:
      for rule in rules:
        print(f"* {rule}")
        time.sleep(0.5)
      understood = ask("Did you understand the rules?(y/n) ")
      if understood:
        break
