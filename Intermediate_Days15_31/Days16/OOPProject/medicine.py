from datetime import datetime


# 创建一个类用来生成Medicine对象
class Medicine(object):

    # 统一的initial函数用来进行实例化
    def __init__(self, name, price, PD, Exp):
        self.name = name
        self.price = price
        self.PD = PD
        self.Exp = Exp

    # 获取名字用的get函数
    def get_name(self):
        return self.name

    # 用来获取GP的函数
    def get_GP(self):
        # 对时间进行格式化
        start = datetime.strptime(self.PD, "%Y-%m-%d")
        end = datetime.strptime(self.Exp, "%Y-%m-%d")
        GP = end - start
        return GP.days

    # 用来判断是否是 expire
    def is_expire(self):
        today = datetime.now()
        oldday = datetime.strptime(self.Exp, "%Y-%m-%d")
        if today > oldday:
            return True
        else:
            return False


if __name__ == '__main__':
    medicineObj = Medicine("阿莫西林", 100, '2019-1-1', '2019-3-1')
    print("name:", medicineObj.get_name())
    print("药品保质期为：", medicineObj.get_GP())
    print("药品是否过期：", "药品过期" if medicineObj.is_expire() else "药品未过期")
