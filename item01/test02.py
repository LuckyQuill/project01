math_list = [30, 60, 15, 45, 7, 1]
i = 0
for t in math_list:
    if i % 2 == 0:
        t *= 2
        print(t)
    elif i % 3 == 0:
        t *= 3
        print(t)
    i += 1
