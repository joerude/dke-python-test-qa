def search(array, target):
    lower = 0
    upper = len(array)

    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x


print(search([1, 3, 5, 7, 8, 2345, 1223, 5], 2345))
