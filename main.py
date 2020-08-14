name = input("What is your name? ")
decision = ("Do you want to play a game?")
ans = input("Use Y or N for your answer. ").lower()
if ans == "y":
  print(name + ", welocme to my world.")
elif ans == "n":
  print("Bye")
else:
  print("You did not answer the question correctly and was only given one chance. Bye.")

