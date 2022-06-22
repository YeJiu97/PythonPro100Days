from random import randint  # 首先导入random包

# 两种不同的难度
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# 对用户的答案进行检测
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

# 设置游戏的难度
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# 游戏的主体函数
def game():

  # 选择一个1~100之间的数字
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
# print(f"Pssst, the correct answer is {answer}") 


  # 存在着多少的剩余猜测次数
  turns = set_difficulty()

  # 让用户来进行猜测
  guess = 0

  # 当猜测不等于答案的时候
  while guess != answer:

  	# 首先告诉用户还有多少剩余的次数进行猜测
    print(f"You have {turns} attempts remaining to guess the number.")

    # 让用户猜测一个数字
    guess = int(input("Make a guess: "))

    # 调用检测函数进行检测
    turns = check_answer(guess, answer, turns)

    # 如果剩余次数为0，则停止
    if turns == 0:
      print("You've run out of guesses, you lose.")
      print(f"The correct answer is {answer}")
      return False
    elif guess != answer:
      print("Guess again.")


game()