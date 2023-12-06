answer = []
answers = [1,2,3,4,5,6,7,8,9,10]

for i in range(10):
    question = input('')
    question.append(answer)

    if answer[i] == answers[i]:
        print('Correct Answer!')
    else:
        print('incorrect answer')
