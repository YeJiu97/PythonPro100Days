class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # 被关注者的followers增加了1，而关注人的following人数增加了1
    def follow(self, user):
        user.followers += 1
        self.following += 1


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    user_1 = User("001", "Jobs")
    user_2 = User("002", "Bob")
    # print(user_1.username)
    # print(user_1.id)
    user_1.follow(user_2)
    print(user_1.followers)
    print(user_1.following)
    print(user_2.followers)
    print(user_2.following)