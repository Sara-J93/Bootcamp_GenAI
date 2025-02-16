import random

class Game:
   def __init__ (self):
      self.user_score = 0 
      self.computer_score = 0

   def get_user_item(self):
      item = input('write "r" for rock, "p" for paper, "s" for scissors:').lower()
      while item not in ["r", "p", "s"]:
         print ("invalid input,  please try again.")
         item = input('write "r" for rock, "p" for paper, "s" for scissors:').lower()
      return item

   def get_computer_item(self):
     choices = ["r", "p", "s"]
     computer_choice = random.choice(choices)
     return computer_choice

   def get_game_result(self, user_item, computer_item):
      if user_item == computer_item:
            return "draw"
        
      elif (user_item == "r" and computer_item == "s") or \
             (user_item == "s" and computer_item == "p") or \
             (user_item == "p" and computer_item == "r"):
            return "win"
        
      else:
            return "loss"

   def play(self):
       while True:  # Loop to keep playing
         user_item = self.get_user_item()  # Get the user's choice
         computer_item = self.get_computer_item()  # Get the computer's choice
         result = self.get_game_result(user_item, computer_item)  # Determine the result

         print(f"You selected {user_item}. The computer selected {computer_item}.", end=" ")

    # Check the result and update the scores
         if result == "win":
          print("You win!")
          self.user_score += 1  # Increment user's score for a win
         elif result == "draw":
          print("It's a draw!")
         else:
          print("You lose!")
         self.computer_score += 1  # Increment computer's score for a loss

    # Display the current scores
         print(f"Score: You {self.user_score} - Computer {self.computer_score}")

    # Ask if the user wants to play again
         play_again = input("Do you want to play again? (y/n): ").lower()
         if play_again != 'y':  # If the user enters anything other than 'y', stop the game
          print("Thanks for playing!")
          break
      #   user_item = self.get_user_item()  
      #   computer_item = self.get_computer_item()  
      #   result = self.get_game_result(user_item, computer_item)       
      #   print(f"You selected {user_item}. The computer selected {computer_item}.", end=" ")
      #   if result == "win":
      #       print("You win!")
      #   elif result == "draw":
      #       print("It's a draw!")
      #   else:
      #       print("You lose!")

      #   return result  

game = Game()
# user_choice = game.get_user_item()
# print ("you selected:", user_choice)
# computer_choice = game.get_computer_item()
# print("Computer selected:", computer_choice)
# result= game.get_game_result(user_choice, computer_choice)
game_result = game.play()

 
