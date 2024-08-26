def has_unique_characters(data):
    my_set = set([])
    for char in data:
        if char in my_set:
            return False
        my_set.add(char)
    return True


print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
