# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = float(weight)/(float(height)*float(height))

print(int(BMI))

# 如果要四舍五入
print(round(BMI))

# 或者我们可以指定多少个小数
print(round(BMI, 2))