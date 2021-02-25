def Fibonacci(num):
    try:
        val = int(num)
    except ValueError:
        return -1
    if num <= 0:
        return -1
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return Fibonacci(num-1)+Fibonacci(num-2)


def Factorial(num):
    try:
        val = int(num)
    except ValueError:
        return -1
    if (num <= 0):
        return -1
    f = 1
    for i in range(1, num+1):
        f = f * i

    return f
