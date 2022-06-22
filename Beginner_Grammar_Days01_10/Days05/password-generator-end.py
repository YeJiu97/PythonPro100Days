# PassWord Generator
import random

# 字母列表
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 数字列表
 numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 符号列表
 symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 要求用户进行输入
print("Welcome to the PyPassword Generator!")

# 需要多少的字符
nr_letters = int(input("How many letters would you like in your password?\n"))

# 需要多少的符号
nr_symbols = int(input(f"How many symbols would you like?\n")) 

# 需要多少的数字
nr_numbers = int(input(f"How many numbers would you like?\n"))


# 创建一个用来存储的列表
password_list = []


# 各个列表中随机选取指定数量的东西
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# 我们可以查看一下列表
print(password_list)

# 进行随机打乱
random.shuffle(password_list)
print(password_list)

# 将列表中的内容提取成为字符串
password = ""
for char in password_list:
  password += char

# 打印字符串
print(f"Your password is: {password}")