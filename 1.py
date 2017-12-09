with open('1.txt', 'r') as f:
    s = f.read().strip()
    n = len(s)
    sum1 = 0
    for i in range(n):
        a, b = s[i%n], s[(i+1)%n]
        if a == b:
            sum1 += int(a)
    sum2 = 0
    for i in range(n):
        a, b = s[i%n], s[(i+(n//2))%n]
        if a == b:
            sum2 += int(a)
    print(sum1, sum2)