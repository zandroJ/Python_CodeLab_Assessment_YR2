def mul_list(list):
    multiplier = 1
    for elements in list:
         ans = multiplier * elements
    return ans

test_list = [2, 2, 2]
print("Result:",mul_list(test_list))
