n = int(input())

numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


def cut_array(start_idx, end_idx):
    global end_of_array

    cut_len = end_idx - start_idx + 1
    for i in range(end_idx + 1, end_of_array):
        numbers[i - cut_len] = numbers[i]

    end_of_array -= cut_len


for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s - 1, e - 1)

print(end_of_array) # 남아있는 블럭의 수 출력
for i in range(end_of_array):
    print(numbers[i])