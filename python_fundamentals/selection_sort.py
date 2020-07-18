# Selection Sort
# Define a function that accepts a list of integers
# Move through the list to find the lowest value
# Move that lowest value to the first position in the list
# Loop through the list again (ignoring any position with a set number) until the list is sorted

def selection_sort(li, flr=0):
    list_len = len(li)
    floor = flr
    min_val = li[floor]
    min_val_i = floor

    for i in range(floor, list_len):
        if li[i] < min_val:
            min_val = li[i]
            min_val_i = i

    li[floor], li[min_val_i] = li[min_val_i], li[floor]
    floor += 1

    if floor == list_len:
        print(li)
    else:
        selection_sort(li, floor)

selection_sort([4,2,3,6,0])