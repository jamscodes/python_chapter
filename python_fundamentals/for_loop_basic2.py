# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggieSize(list):
#     for num in range(len(list)):
#         if list[num] > 0:
#             list[num] = "big"
#     return list

# print(biggieSize([-1,3,4,-5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def countPositives(list):
#     positiveCount = 0

#     for num in list:
#         if num > 0:
#             positiveCount += 1
    
#     list[-1] = positiveCount
#     return list

# print(countPositives([-1,1,1,1]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sumTotal(list):
#     sum = 0

#     for num in list:
#         sum += num
    
#     return sum

# print(sumTotal([6,3,-2]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def average(list):
#     sum = 0
#     for num in list:
#         sum += num
#     return sum / len(list)

# print(average([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(list):
#     return len(list)

# print(length([37,2,1,-9]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(list):
#     if len(list) == 0:
#         return False

#     minVal = list[0]

#     for num in list:
#         if num < minVal:
#             minVal = num

#     return minVal

# print(minimum([37,2,1,-9]))


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(list):
#     if len(list) == 0:
#         return False

#     maxVal = list[0]

#     for num in list:
#         if num > maxVal:
#             maxVal = num

#     return maxVal

# print(maximum([37,2,1,-9]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimateAnalysis(list):
#     newDict, sum, min, max = {}, 0, list[0], list[0]

#     for num in list:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#         sum += num
    
#     newDict.update({
#         'sumTotal': sum,
#         'average': sum / len(list),
#         'minimum': min,
#         'maximum': max,
#         'length': len(list)
#     })

#     return newDict

# print(ultimateAnalysis([37,2,1,-9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverseList(list):
#     list.reverse() # I guess this counts as a "built in" solution and not a "skilled" solution
#     return list

# def reverseList(list):
#     countdown = len(list) - 1
#     countup = 0

#     while countup < countdown:
#         temp = list[countdown]

#         list[countdown] = list[countup]
#         list[countup] = temp

#         countup += 1
#         countdown -= 1
    
#     return list

# def reverseList(list):
#     countdown = len(list) - 1
#     for x in range(0, countdown):
#         temp = list[countdown]

#         list[countdown] = list[x]
#         list[x] = temp

#         countdown -= 1
#     return list

# print(reverseList([37,2,1,-9]))