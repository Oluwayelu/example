'''
This function takes in a specific number of guesses and target number
and returns the difference between the user's final guess and actual value 
'''

def guessGame(no_of_guess, target_no):
  for i in range(no_of_guess):
    guess = int(input("Enter number btw. 0 to 100: "))
    if(guess < 0 or guess > 100):
      print("number out of range")
    else:
      if(guess > target_no):
        print("Reduce your number")
      elif(guess < target_no):
        print("Increase your number")
      else:
        print("You got the correct number")
        break
  
  print("Differece between your final number and the target number is " + str(abs(guess - target_no)))
      
#test
guessGame(3, 50)
