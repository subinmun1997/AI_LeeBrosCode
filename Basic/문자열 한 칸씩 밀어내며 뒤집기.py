input_str, q = tuple(input().split())
q = int(q)


def shift_front():
    global input_str
    input_str = input_str[1:] + input_str[0]

    print(input_str)


def shift_back():
    global input_str
    input_str = input_str[-1] + input_str[:-1]

    print(input_str)


def reverse():
    global input_str
    input_str = input_str[::-1]

    print(input_str)


for _ in range(q):
    q_type = int(input())
    if q_type == 1:
        shift_front()
    elif q_type == 2:
        shift_back()
    elif q_type == 3:
        reverse()
