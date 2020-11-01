# Countdown

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


# Countup

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


# My function

number = int(input("Type the number: "))

def my_function(n):
    if n > 0:
        countdown(n)
    elif n < 0:
        countup(n)
    else:
        print('Blastoff!')


my_function(number)
