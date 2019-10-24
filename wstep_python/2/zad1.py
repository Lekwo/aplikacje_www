def f(a_list, b_list):
    list = []
    for i in range(0, len(a_list)):
        if i % 2:
            list.append(a_list[i])
    for i in range(0, len(b_list)):
        if not i % 2:
            list.append(b_list[i])
    return list


a_list = [i for i in range(1, 19)]
b_list = [i for i in range(26, 48)]
print(f(a_list, b_list))
