imin = 0
imax = 0

array = list(range(10))
size = len(array)
for i in range(size):
    if array[i] < array[imin]:
        imin = i
    elif array[i] > array[imax]:
        imax = i

print(imin, imax)
