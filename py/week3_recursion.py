def fibonacci(n):
    # Fn = Fn - 1 + Fn - 2
    if n < 0:
        print("Incorrect input") 
    # fibonacci(1) number is 0
    elif n == 1:
        return 0
    # fibonacci(2) number is 1
    elif n == 2:
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


if __name__ == '__main__':
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    print(fibonacci(10))
    print(fact(4))
