#Color and Special text formats
class text:
  BOLD = '\033[1m'
  BLUE = '\033[94m'
  RED = '\033[91m'
  END = '\033[0m'

#Starting score 
score = 0

print(text.RED + 'This is a yes and no quiz. All answers will be in a ' + text.BOLD + 'Yes and No ' + 'format' + text.END)

# Question 1 
answer1 = input(text.BLUE + 'Were you at the Macdonald Hotel at Fairmont on the night of the murder? ' + text.END)
if answer1 == "yes" or answer1 =="Yes":
    score = score + 1

#Question 2 
answer2 = input(text.BLUE + 'Did you know Daniel? ' + text.END )
if answer2 == "yes" or answer2 =="Yes":
    score = score + 1

#Question 3
answer3 = input(text.BLUE + 'Do you confess to the murder of Daniel? ' + text.END)
if answer3 == "no" or answer3 =="No":
    score = score + 1

#Question 4
answer4 = input(text.BLUE + 'Would you like to speak to your lawyer? ' + text.END)
if answer4 == "yes" or answer4 =="Yes":
  score = score + 1

#Final Result
print(text.RED + 'Your score is ' + str(score) + " / 4" + text.END)
percentage = score / 4 * 100
print(text.RED + 'percentage' + text.END)

if score == 4:
  print(text.RED + 'You are free to go' + text.END)
elif score == 3:
  print(text.RED + 'You are a person of interest' + text.END)
elif score == 2:
    print(text.RED + 'You are the main Suspect' + text.END)
else: 
  print(text.RED + 'You are arrested' + text.END)