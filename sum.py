number_list = [1, 2, 3, 4, 5]

def list_sum(lists):
    sum = 0
    for number in lists:
        sum += number
    return sum

print(list_sum(number_list))