def f(x):
    result = 0
    for i in range(1000):
        result+=1
    for i in range(x):
        result+=1
    for i in range(x):
        for j in range(x):
            result+=1
            result+=1
    return result
print(f(100))