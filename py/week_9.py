import datetime


def recursion_fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)


memo = {
    0: 0,
    1: 0,
    2: 1,
}


def dp_fibonacci(n):
    if n in memo:
        return memo[n]
    memo[n-1] = dp_fibonacci(n-1)
    memo[n-2] = dp_fibonacci(n-2)
    memo[n] = dp_fibonacci(n-1) + dp_fibonacci(n-2)
    return memo[n]


if __name__ == '__main__':
    start = datetime.datetime.now()
    print(recursion_fibonacci(35))
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()
    print(dp_fibonacci(35))
    print(datetime.datetime.now() - start)
