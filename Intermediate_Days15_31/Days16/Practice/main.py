# module可以是我们本地自己创建的
import another_module

# moduleName.moduleVariable 或者 moduleName.moduleFunction
# 可以用来调用module种的对应的variable或者function
print(another_module.another_variable)

# 从turtle这个module种导入Turtle这个class
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

# 我们将timmy的形状设置为turtle
timmy.shape("turtle")

# 我们再来尝试一下对颜色进行设置
timmy.color("blue")

# 接着让我们尝试着将这个turtle往某一个方向移动一段距离
timmy.forward(another_module.another_variable)

# 或者我们来画一个圈
# timmy.circle(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

# 可以让我们代码运行的图片能够保持一段时间
# my_screen.exitonclick()  # on click的时候会导致exit

# 尝试一下prettytable
from prettytable import PrettyTable

tableOne = PrettyTable()
tableOne.add_column("Pokeman Name", ["Pikachu", "Squirrel", "Charmane"])
print(tableOne)
tableOne.add_column("Type", ["Electric", "Water", "Fire"])
print(tableOne)
tableOne.add_column("Value", [10, 20, 15])
print(tableOne)
