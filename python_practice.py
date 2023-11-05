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

triangle = [[1],[1,1]]

def pascal(n):
  if n < 1:
    print("Null")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)    

pascal(7)