# def greet(name, age):
# 	print(f"Hi, {name}.")
# 	print(f"Happy birthday!, you are {age} now.")

# greet(name="小张", 16)  # 这样是会报错的，因为positional argument排在了keyword argument之后了。

# 我们可以进行这样的尝试

def greet(name, age, tel):
	print(f"Hi, {name}.")
	print(f"Happy birthday!, you are {age} now.")
	print(f"You can call {tel} to get a gift.")

greet("小张", tel=123654, age=16)