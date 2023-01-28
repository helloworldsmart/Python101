# 6.1
for x in list(range(3, -1, -1)):
    print(x)

# 6.2
guess_me = 7
number = 1

# My answer
# while number == guess_me:
#     print('found it!')
#     break
# else :
#     if number < guess_me:
#         print('too low')
#         continue
#     else:
#         print('oops')
#     break

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me: # can don't has eles ?
        print('oops')
        break
    number += 1

print('---')
# 6.3
# My answer
guess_me_2 = 5
for number in range(10):
    if number < guess_me_2:
        print('too low')
    elif number == guess_me_2:
        print('found it!')
        break
    else:
        print('oops')
        break
