import random
import state_capitals

for seed in range(1, 3):
    random.seed(seed)
    print('Quiz #{}'.format(seed))
    quizfile = open(f'capitalsquiz{seed}.txt', 'w')
    answerfile = open(f'capitalsquiz{seed}_answers.txt', 'w')
    quizfile.write('Quiz #{}\n\nName:\n\nDate:\n\n'.format(seed))
    answerfile.write('Quiz #{} Answer Key'.format(seed))
    quizfile.close()
    answerfile.close()
    for state in random.sample(list(state_capitals.capitals.keys()), 3):
        quizfile = open(f'capitalsquiz{seed}.txt', 'a')
        answerfile = open(f'capitalsquiz{seed}_answers.txt', 'a')
        Question = []
        Choices = []
        Question.append('What is the capital of {}?'.format(state))
        Choices.append(state_capitals.capitals[state])
        for a in range(0, 3):
            Choices.append(
                random.choice([x for x in state_capitals.capitals.values() if x != state_capitals.capitals[state]]))
        quizfile.write('{}\n{}\n\n'.format(Question[0], random.sample(Choices, 4)))
        answerfile.write('{}\nAnswer: {}\n\n'.format(Question[0], state_capitals.capitals[state][0]))
        print(Question, random.sample(Choices, 4))
        print('Answer: {}'.format(state_capitals.capitals[state]))

    print('\n')
