math_list = [30, 60, 15, 45, 7, 1, 75, 20, 25]
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
    if t <= 30:
        print(f"气笑了:{t}")
    else:
        print(f"哈气了:{t}")
    i += 1

print(i)
