math_list = [30, 60, 15, 45, 7, 1]
i = 1
for t in math_list:
    print(f"现在是第{i}次")
    if i % 2 == 0:
        t *= 2
        print(t)
    elif i % 3 == 0:
        t *= 3
        print(t)
    else:
        print(t * 5)
    i += 1

print(i)
