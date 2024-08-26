from collections import deque


def print_binary_numbers(n):
    if n <= 0:
        return
    my_queue = deque()
    for i in range(1, n+1):
        my_queue.append(bin(i))
    while len(my_queue) > 0:
        print(my_queue.popleft()[2:])


print_binary_numbers(6)
print()
print_binary_numbers(-9)
print()
print_binary_numbers(0)
print()
print_binary_numbers(2)
print()
print_binary_numbers(10)
