# Recursion with infinite loop
# It will run forever
# Ctrl-C to kill script

def countdown(i):
    print(i)
    countdown(i - 1)


countdown(5)
