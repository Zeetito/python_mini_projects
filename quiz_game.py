print("Welcome Player!")

name = input("Enter your name: ")

print ('Hello ' + name + '!')

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print('Okay, Lets play!')
score = 0
q = 0

answer = input('What does CPU stands for? ')
q+=1
if answer.lower() == 'central processing unit':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('What does GPU stands for? ')
q+=1
if answer.lower() == 'graphics processing unit':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('What does RAM stands for? ')
q+=1
if answer.lower() == 'random access memory':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input('What does PS stands for? ')
q+=1
if answer.lower() == 'power supply':
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct' + ' out of ' + str(q) + ' questions')