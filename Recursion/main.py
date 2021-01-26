def count(number):
    if number < 0:
        return # stops the recursion
    print(number)
    count(number-1)


def count_iterative(number):
    while number >= 0:
        print(number)
        number -= 1

# terribly slow and bad, counts a bunch of ones
def fib(nth):
    if nth < 2:
        return 1
    return fib(nth-1) + fib(nth-2)


def _better_fib(nth, current_nth, previous, current):
    if nth == current_nth:
        return previous + current
    return _better_fib(nth, current_nth+1, current, previous+current)


def better_fib(nth):
    if nth < 2:
        return 1
    return _better_fib(nth, 2, 1, 1)


for n in range(40):
    print(n, ":", better_fib(n))