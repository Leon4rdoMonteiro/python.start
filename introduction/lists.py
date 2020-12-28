# LISTS

pair_numbers = [0, 2, 4 , 6, 8]
odd_numbers = [1, 3, 5, 7, 9]

def sum_lists_numbers(list1, list2):
    total = 0

    # Join lists
    list = list1 + list2  

    # Remove an element by value
    list.remove(0)

    # Remove an element by index
    del(list[4])

    # Add an element
    list.append(1)

    for number in list:
        total += number
    
    return total

numbers = sum_lists_numbers(pair_numbers, odd_numbers)

print(numbers)