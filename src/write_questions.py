from random import randint, shuffle#every variable name should follow its filename + '_' to avoid overlapping with potential 
#future variable names for other files

#basic_addition
basic_addition_first, basic_addition_second = randint(0, 9), randint(0, 9)
basic_addition_answer =  basic_addition_first + basic_addition_second
basic_addition_answers = [basic_addition_answer]
basic_addition_range = randint(1, 3)

for i in range(1, basic_addition_range+1):
    basic_addition_answers.append(basic_addition_answer + i)
for i in range(1, 4-basic_addition_range):
    basic_addition_answers.append(basic_addition_answer - i)

shuffle(basic_addition_answers)


print(f"What is {basic_addition_first} + {basic_addition_second}?: {basic_addition_answers[0]}, {basic_addition_answers[1]}, {basic_addition_answers[2]}, {basic_addition_answers[3]}")

basic_addition_file = open('src\\answers\\Mathematics\\basic_addition.txt', 'w')
basic_addition_file.write(f"What is {basic_addition_first} + {basic_addition_second}?: {[int(answer) for answer in basic_addition_answers]}")
basic_addition_file.close()