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
possibleChooses = ["Rock", "Paper","Scissors"]
def wait(): 
  time.sleep(0.5)
def wait1():
  time.sleep(1)
def ask(text):
   while True:
    ask = input(text)
    if ask == "y":
      return True
    if ask == "n":
      return False
# if ask("Do you want to know the rules?(y/n) "):
#    while True:
#       for rule in rules:
#         print(f"* {rule}")
#         wait()
#       understood = ask("Did you understand the rules?(y/n) ").lower()
#       if understood:
#         break
# while True:
#   print("Select difficulty:")
#   wait()
#   print("- Easy(E)")
#   wait()
#   print("- Normal(N)")
#   wait()
#   print(f"- {Fore.RED}{Style.BRIGHT}Impossible(I)")
#   level = input("$ ").lower()
#   if level == "n" or level == "normal":
#     print(f"You choose {Style.BRIGHT}normal{Style.RESET_ALL} difficulty!")
#     break
#   if level == "e" or level == "easy":
#     print(f"You choose {Style.BRIGHT}easy{Style.RESET_ALL} difficulty!")
#     break
#   if level == "i" or level == "impossible":
#     print(f"You choose {Fore.RED}{Style.BRIGHT}IMPOSSIBLE{Style.RESET_ALL} difficulty!")
#     break
# print("------------------------")
# wait1()
level = "n"
playerScore = 0
computerScore = 0
def whoWins(playerChoose):
   computerChoose = random.choice(possibleChooses)
   if playerChoose == "Scissors":
    if computerChoose == "Rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        if restart == False:
          print("Thanks for playing")
          exit()
    elif computerChoose == "Paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL}!")
      playerScore += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
    elif computerChoose == "Scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL} too!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
   if playerChoose == "Paper":
    if computerChoose == "Scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        if restart == False:
          print("Thanks for playing")
          exit()
    elif computerChoose == "Rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
    elif computerChoose == "Paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL} too!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
   if playerChoose == "Rock":
    if computerChoose == "Paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL}!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        if restart == False:
          print("Thanks for playing")
          exit()
    elif computerChoose == "Scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
    elif computerChoose == "Rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL} too!")
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          print("Thanks for playing!")
          exit()
while level == n or level == normal:
  print("So, let's play! ....")
  wait1()
  print("Rock")
  wait1()
  print("Paper")
  wait1()
  print("Scissors")
  wait1()
  print("Shoot!")
  playerChoose = input("> ")
  whoWins(playerChoose)