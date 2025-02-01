import colorama,time,random
from colorama import Style, Back, Fore, init
init(autoreset=True)
print(f"{Fore.YELLOW}{Style.BRIGHT}# Rock, paper and scissors")
understood = 0
rules = [
   f"A {Fore.YELLOW}{Style.BRIGHT}Rock beats scissors{Style.RESET_ALL} by smashing them",
   f"{Fore.YELLOW}{Style.BRIGHT}Scissors beats paper{Style.RESET_ALL} by cutting it",
   f"{Fore.YELLOW}{Style.BRIGHT}Paper beats rock{Style.RESET_ALL} by covering it"
]
possibleChooses = ["rock", "paper","scissors"]
def wait(): 
  time.sleep(0.5)
def wait1():
  time.sleep(1)
def ask(text):
   while True:
    ask = input(text).lower()
    if ask == "y":
      return True
    if ask == "n":
      return False
def scoreboard(playerScore,computerScore):
  scoreboard = f"""
          ╔════════════════╗
          ║   {Fore.YELLOW}{Style.BRIGHT}SCOREBOARD{Style.RESET_ALL}   ║
          ╚════════════════╝
          Player :  {Fore.YELLOW}{Style.BRIGHT}{playerScore}{Style.RESET_ALL}
          Computer:  {Fore.YELLOW}{Style.BRIGHT}{computerScore}{Style.RESET_ALL}
          """
  print(scoreboard)
if ask("Do you want to know the rules?(y/n) "):
   while True:
      for rule in rules:
        print(f"* {rule}")
        wait()
      understood = ask("Did you understand the rules?(y/n) ")
      if understood:
        break
while True:
  print("Select difficulty:")
  wait()
  print("- Easy(E)")
  wait()
  print("- Normal(N)")
  wait()
  print(f"- {Fore.RED}{Style.BRIGHT}Impossible(I)")
  level = input("> ").lower()
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
wait1()
playerScore = 0
computerScore = 0
def whoWins(playerChoose):
   computerChoose = random.choice(possibleChooses)
   if playerChoose == "scissors":
    if computerChoose == "rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
      globals()["computerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL}!")
      globals()["playerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL} too!")
      globals()["playerScore"] += 1
      globals()["computerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
   if playerChoose == "paper":
    if computerChoose == "scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
      globals()["computerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        if restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
      globals()["playerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL} too!")
      globals()["computerScore"] += 1
      globals()["playerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
   if playerChoose == "rock":
    if computerChoose == "paper":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}paper{Style.RESET_ALL}!")
      globals()["computerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        if restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "scissors":
      print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
      globals()["playerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
    elif computerChoose == "rock":
      print(f"{Fore.YELLOW}{Style.BRIGHT}Draw{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL} too!")
      globals()["playerScore"] += 1
      globals()["computerScore"] += 1
      while True:
        restart = ask("Do you want to play again?(y/n) ")
        if restart == True:
          break
        elif restart == False:
          scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
          if scoreboardAsk:
            print("Okay, I'll show you the scoreboard, wait a minute")
            wait()
            scoreboard(playerScore, computerScore)
          print("Thanks for playing!")
          while True:
            enter = input("Press ENTER to exit...")
            if enter == "":
              exit()
def impossibleToWin(playerChoose):
  if playerChoose == "rock":
    computerChoose = "paper"
    print(f"{Fore.RED}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.RED}{Style.BRIGHT}paper{Style.RESET_ALL}!")
    globals()["computerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
  if playerChoose == "paper":
    computerChoose = "scissors"
    print(f"{Fore.RED}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.RED}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
    globals()["computerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
  if playerChoose == "scissors":
    computerChoose = "rock"
    print(f"{Fore.RED}{Style.BRIGHT}You lose{Style.RESET_ALL}, I choose {Fore.RED}{Style.BRIGHT}rock{Style.RESET_ALL}!")
    globals()["computerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
def easyToWin(playerChoose):
  if playerChoose == "rock":
    computerChoose = "scissors"
    print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}scissors{Style.RESET_ALL}!")
    globals()["playerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
  if playerChoose == "paper":
    computerChoose = "rock"
    print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
    globals()["playerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
  if playerChoose == "scissors":
    computerChoose = "paper"
    print(f"{Fore.YELLOW}{Style.BRIGHT}You won{Style.RESET_ALL}, I choose {Fore.YELLOW}{Style.BRIGHT}rock{Style.RESET_ALL}!")
    globals()["playerScore"] += 1
    while True:
      restart = ask("Do you want to play again?(y/n) ")
      if restart:
        break
      elif restart == False:
        scoreboardAsk = ask("Before you leave, do you want to see the scoreboard?(y/n) ")
        if scoreboardAsk:
          print("Okay, I'll show you the scoreboard, wait a minute")
          wait()
          scoreboard(playerScore,computerScore)
        print("Thanks for playing!")
        while True:
          enter = input("Press ENTER to exit...")
          if enter == "":
            exit()
while level == "n" or level == "normal":
  print("So, let's play! ....")
  wait1()
  print("Rock")
  wait1()
  print("Paper")
  wait1()
  print("Scissors")
  wait1()
  print("Shoot!")
  playerChoose = input("> ").lower()
  whoWins(playerChoose)
while level == "i" or level == "impossible":
  print("So, let's play! ....")
  wait1()
  print("Rock")
  wait1()
  print("Paper")
  wait1()
  print("Scissors")
  wait1()
  print("Shoot!")
  playerChoose = input("> ").lower()
  impossibleToWin(playerChoose)
while level == "e" or level == "easy":
    print("So, let's play! ....")
    wait1()
    print("Rock")
    wait1()
    print("Paper")
    wait1()
    print("Scissors")
    wait1()
    print("Shoot!")
    playerChoose = input("> ").lower()
    easyToWin(playerChoose)