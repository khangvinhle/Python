# ChieuCao = int(input('may cao bao nhieu?'))
# if (ChieuCao > 150):
#     print('May cao that day!')
# if (ChieuCao >= 56):
#     print('ok!')
# else:
#     print('thap qua!')

# Traffic light example
# light_color = input('What color is the traffic light? ')
# light_color = light_color.lower()
# print(light_color)
# if light_color == 'red':
#     print('You should stop')
# elif light_color == "yellow":
#     print('Slow down!')
# elif light_color == "green":
#     print('Go ahead!')
# else:
#     print('What country are you in??')

# loop_examples
# helloWord = 'Hello world'
# letter_count = 0
# for letter in helloWord:
#     print('letter number ', letter_count, ' is ', letter)
#     letter_count += 1
# print('there were ', letter_count, ' in the string ', helloWord)

# for num in range(7, 15):
#     print(num)

# for num in range(0, 10, -2):
#     print(num)

# while loop example
count = 1
print('count is initially ', count)
while count < 100:
    count = count * 9
    print('now count is ', count)
    if count >= 100:
        print('Now >= 100, exit loop')
print('count is ', count)
