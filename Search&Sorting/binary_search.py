"""
Binary Search Algorithm
- Given sorted list find element x
  return True if he exist and False if it does not
"""


def binary_search(arr, x):
    if not arr:
        return None

    if arr[len(arr)/2] == x:
        return True

    if x > arr[len(arr)/2]:
        return binary_search(arr[len(arr)//2:], x)

    return binary_search(arr[:len(arr)//2], x)


myArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1,10):
    print(binary_search(myArr, i))
