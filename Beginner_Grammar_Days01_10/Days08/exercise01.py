#Write your code below this line π
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)  # ceil()ε½ζ°ε―δ»₯η¨ζ₯εδΈθΏθ‘εζ΄
    print(f"You'll need {round_up_cans} cans of paint.")


#Write your code above this line π
# Define a function called paint_calc() so that the code below works.   

# π¨ Don't change the code below π
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)