# Python没有为int提供len函数求取长度
# 但是我们可以这么做
num = 123321
print(len(str(num)))

# string的可以使用[n]来访问第n-1个位置的字符
# 从0开始
print(str(num)[0])

# 我们可以使用type()函数来获取变量的类型
strNumber = 123321
print(type(strNumber))

strNumber2 = input("请输入一个数字：")
print(type(strNumber2))  # 判断的结果是string类型

