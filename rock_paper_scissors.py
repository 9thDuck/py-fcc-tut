import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

its_a_tie = "It's a tie!"
computer_wins = 'Computer Wins!'
player_wins = 'You Win!'

def get_choices():
  options = [rock, paper, scissors]
  player_choice = input('Enter a choice (rock, paper, scissors): ')
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  def print_choices():
   print(f'You chose: {player}. Computer chose: {computer}.')

  if player == computer:
    return its_a_tie
  elif player == rock:
   print_choices()
   if computer == scissors:
    return f'Rock crushes scissors. {player_wins}'
   else:
    return f'Paper covers rock. {computer_wins}'

  elif player == paper:
   print_choices()
   if computer == scissors:
    return f"Scissors cuts paper. {computer_wins}"
   else:
    return f"Paper covers rock. {player_wins}"

  elif player == scissors:
   print_choices()
   if computer == paper:
    return f'Scissors cuts paper. {player_wins}'
   else:
    return f'Rock crushes scissors. {computer_wins}'
  else: return f'You have entered invalid input. Please enter one of the given words.'


def play_rock_paper_scissors():

 choices = get_choices()
 result = check_win(choices['player'], choices['computer'])
 print(result)


