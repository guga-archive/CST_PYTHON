def fibonacci(n, d):
    if n in d:
        return d[n]
    else:
        answer = fibonacci(n-1, d) + fibonacci(n - 2, d)
        d[n] = answer
        return answer
        
d = {1:1, 2:2}
print(fibonacci(10, d))