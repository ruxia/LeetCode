def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    res = fibonacci(n-1) + fibonacci(n-2)
    return res

if __name__ == '__main__':
    print(fibonacci(8))
