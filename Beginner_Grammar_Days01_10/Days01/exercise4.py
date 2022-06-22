'''
Example Input
a: 3
b: 5
Example Output
a: 5
b: 3
'''

a = input("a: ")
b = input("b: ")

a, b, = b, a

print("a: " + a)
print("b: " + b)