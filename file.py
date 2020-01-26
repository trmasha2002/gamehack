def FUNC(a=0, c=2):
    print(a)


def FUNC2(a=1, c=2):
    print(c)


FUNC()
FUNC2()
max_n = 100
left = 0
right = 100
while(right - left > 1):
    m = ((left + right) // 2)
    if (m <= x):
        left = m
    else:
        right = m
print(left)
