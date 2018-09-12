# Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”,
# пока он не ответит “Хорошо”. Создайте словарь типа "вопрос": "ответ", например:
# {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее.
# Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему
# соотвествующий ответ. Например:
# Пользователь: Что делаешь?
# Программа: Программирую


def ask_user(questions_answers):
    user_say = str(input('Как дела? \n>>'))
    while True:
        try:
            if questions_answers.get(user_say):
                user_say = str(input(questions_answers[user_say] + '\n>>'))
                continue
            elif user_say == 'Хорошо':
                break
            else:
                user_say = str(input('Как дела? \n>>'))
                continue
        except KeyboardInterrupt:
            print('\nПока!')
            break


answers_dict = {"Привет": "Привет!", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую",
                "На каком языке?": "Естественно, на Python!"}
if __name__ == '__main__':
    ask_user(answers_dict)
