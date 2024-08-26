def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    
    my_num = max(my_list)
    my_min = min(my_list)
    for item in my_list:
        if my_num > item > my_min:
            my_num = item
    return my_num


print(find_second_smallest([5, 8, 3, 2, 6]))
