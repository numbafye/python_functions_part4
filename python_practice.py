def max_num(a, b, c):
    return max([a, b, c])

print(max_num(99, 22, 33))

def mult_list(list):
    if len(list) == 0:
        return 0
    nums = list[0]

    if len(list) > 1:
    # iterate after nums index "0"
        for i in list[1:]:
            nums = nums * i
    return nums

print(mult_list([5, 5, 5]))

def rev_string(string):
    return string[::-1]

print (rev_string("DOG"))
    

def num_within(a, b, c):
    return c in range(a, b+1)

print(num_within(1,7,10))
print(num_within(1,7,5))
