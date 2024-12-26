number_list = [1, 2, 3, 4, 5]

def largest(lists):
    max = 0
    for number in lists:
        if number >= max:
            max = number
    return max

max = largest(number_list)
print(f"The maximus number is {max}")