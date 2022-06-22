# 导入三个modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    # 创建一个question bank列表，用来存储问题
    question_bank = []

    # 将从data中导入的question_data进行遍历
    for question in question_data:
        # 将问题部分赋值给question_text
        question_text = question["question"]
        # 将答案部分赋值给question_answer
        question_answer = question["correct_answer"]
        # 通过quiz_brain中提供的Question函数形成一个问题和题解
        new_question = Question(question_text, question_answer)
        # 将这个新的问题和回答添加到question_bank列表中
        question_bank.append(new_question)

    # 调用quiz_brain中的QuizBrain类
    # 这样一来quiz就是一个 QuizBrain类型 的对象了，可以使用QuizBrain提供的各种method
    quiz = QuizBrain(question_bank)

    #
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
