#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. π²
import random
   
# π¨ Don't change the code below π
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # π¨ Don't change the code above π It's only for testing your code.
   
#Write the rest of your code below this line π
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


# ζθζδ»¬δΉε―δ»₯θΏδΉε
print("Heads" if random.randint(0, 1) == 1 else "Tails")