math_list = [30, 60, 15, 45, 7, 1, 75, 20, 25]
math2_list = []
math3_list = []
i = 1
for t in math_list:
    print(f"现在是第{i}次")
    if i % 2 == 0:
        t *= 2
        math2_list.append(t)
    elif i % 3 == 0:
        t *= 3
        math3_list.append(t)
    else:
        print(t * 5)
    if t <= 30:
        print(f"气笑了:{t}")
    else:
        print(f"哈气了:{t}")
    i += 1

print(i)
print(math2_list)