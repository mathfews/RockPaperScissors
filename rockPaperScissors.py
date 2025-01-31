import colorama,time,random
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"{Fore.YELLOW}{Style.BRIGHT}# Rock, Paper and Scissors")
understood = 0
rules = [
   f"A {Fore.YELLOW}{Style.BRIGHT}Rock beats scissors{Style.RESET_ALL} by smashing them",
   f"{Fore.YELLOW}{Style.BRIGHT}Scissors beats paper{Style.RESET_ALL} by cutting it",
   f"{Fore.YELLOW}{Style.BRIGHT}Paper beats rock{Style.RESET_ALL} by covering it"
]
possibleMoves = ["Rock", "Paper","Scissors"]
def wait(n):
  time.sleep(n)
time = 0.5
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
        wait(time)
      understood = ask("Did you understand the rules?(y/n) ")
      if understood:
        break
while True:
  print("Select difficulty:")
  wait(time)
  print("- Easy(E)")
  wait(time)
  print("- Normal(N)")
  wait(time)
  print(f"- {Fore.RED}{Style.BRIGHT}Impossible(I)")
  level = input("$ ").lower()
  if level == "n" or level == "normal":
    print(f"You choose {Style.BRIGHT}normal{Style.RESET_ALL} difficulty!")
    break
  if level == "e" or level == "easy":
    print(f"You choose {Style.BRIGHT}easy{Style.RESET_ALL} difficulty!")
    break
  if level == "i" or level == "impossible":
    print(f"You choose {Fore.RED}{Style.BRIGHT}IMPOSSIBLE{Style.RESET_ALL} difficulty!")
    break
print("------------------------")
print("So, let's play!")
wait(time)
print("...")
print("Rock")
print("Paper")
print("Scissors")
print("Shoot!")