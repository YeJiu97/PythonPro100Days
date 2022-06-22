import time
import prettytable as pt

# 初始设置为0
money = 0
account_logs = []


class Account():
    # 初始化函数
    def __init__(self):
        global money
        self.money = money
        self.account_logs = account_logs

    def deposit(self):
        amount = float(input("存入金额："))
        self.money += amount
        self.write_log(amount, "转入")

    def withdrawl(self):
        amount = float(input("取出金额为："))
        if amount > self.money:
            print("余额不足")
        else:
            self.money -= amount
            self.write_log(amount, "取出")

    def transaction_log(self):

        tb = pt.PrettyTable()  # 用prettytable来生成一个实例
        tb.field_names = ["交易日期", "摘要", "金额", "币种", "余额"]

        for info in self.account_logs:
            if info(1) == "转入":
                amount = '+{}'.format(info[2])
            else:
                amount = '-{}'.format(info[2])
            tb.add_row([info[0], info[1], amount, "人民币", info[3]])

    def write_log(self, amount, handle):
        create_time = time.strptime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        data = [create_time, handle, amount, self.money]
        self.acount_logs.append(data)


def show_menu(self):

        menu = """
        ========================银行账户资金交易管理====================
        1 ：退出
        2 ：存款
        3 ：取款
        4 ：打印交易详情
        =============================================================
        """

        print(menu)


if __name__ == '__main__':
    show_menu()
    account = Account()
    while True:
        choice = int(input("请输入您的选择: "))
        if choice == 0:
            exit(0)
            print("退出系统")
        elif choice == 1:
            flag = True
            while flag:
                account.deposit()
                flag = True if input("是否继续存款(Y|N): ").lower()== 'y' else False
        elif choice == 2:
            flag = True
            while flag:
                account.withdrawl()
                flag = True if input("是否继续取款(Y|N): ").lower()== 'y' else False
        elif choice == 3:
            account.transaction_log()
        else:
            print("请选择正确的编号")