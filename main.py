from controls import *
import time

# TOS
with open('tos', 'r') as f:
    tos = f.readline(1)
    print(tos)

print(tos)
if tos != "t":
    print("By accepting the TOS, you agree to the following:\nNot using this program for personal purposes.\nI will use"
          " this program on 5 shorts MAXIMUM\nIf any unwanted behaviour occurs, I will open a issue located here:"
          "https://github.com/VACLST/ytshortsbot/issues\nAfter I enter the comment the program will wait 3 secs.")
    acceptTos = input('Do you accept? (y/n) ')
    if acceptTos == 'y':
        with open('tos', 'w') as f:
            f.write('t')
    else:
        print("Accept the TOS.")
        exit(2)

print()
comment = input('What would you like to comment? ')
time.sleep(3)

# Move to the comment button
press('tab', 7)
press('return')
time.sleep(1)
press('tab', 2)
write(comment)
