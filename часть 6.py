# # 6.1
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# # 6.2
# def bubble_sort(array):
#     n = len(array)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 swapped = True
#         if not swapped:
#             break
#     return array