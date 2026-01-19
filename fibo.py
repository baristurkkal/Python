cube = lambda x: x * x * x # complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    fn = []
    if n == 1 :
        fn.append(0)
    elif n > 1 :
        i = 2
        fn.extend([0, 1])
        while i < n :
            tmp = fn[i-1] + fn[i-2]
            fn.append(tmp)
            i = i + 1
    return fn
if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))
  #  print(list(map(cube, fibonacci(n))))
