class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # 用来判断问题是否全部解决

    def next_question(self):
        current_question = self.question_list[self.question_number]  # 通过self.question_number来获取当前的索引位置
        self.question_number += 1  # 接着将这个序列的值增加1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  # 让用户进行输入
        self.check_answer(user_answer, current_question.answer)  # 调用check_answer()函数来进行检测，传入用户的answer和问题的answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # 注意大小写，所以统一转换成小写字母，使用.lower()函数来进行
            self.score += 1  # 如果回答正确，+1分数
            print("You got it right!")
        else:
            print("That's wrong.")  # 否则不+1
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")  # 一题一分，所以当前的总分就等于当前的问题号
        print("\n")
