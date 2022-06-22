#  测试一下global variable
def globalVariable(number):
    """传入一个数字，并且将其修改为global variable"""
    global result
    result = number + 100
    print(result)


globalVariable(10)
print(result)