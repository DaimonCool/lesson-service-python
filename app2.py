def absoluteValuesSumMinimization(arr: list):
    dict = {}
    for val in arr:
        sum = 0
        for inner_val in range(arr.__len__()):
            sum = sum + abs(val - arr[inner_val])
        dict[val] = sum
    print(dict)
    return min(dict, key=dict.get)

print(absoluteValuesSumMinimization([2, 4, 7]))
