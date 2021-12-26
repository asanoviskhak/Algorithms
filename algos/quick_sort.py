def quick_sort(arr):
  if (len(arr)<2):
    return arr
  else:
    pivot  = arr[0]
    smallerList = []
    biggerList = []
    for i in range(1, len(arr)):
      if (arr[i]<pivot):
        smallerList.append(arr[i])
      else:
        biggerList.append(arr[i])
    return quick_sort(smallerList)+[pivot]+quick_sort(biggerList)

# test_list = [1, 6, 3, 5, 3, 1, 5, 6, 4, 2, 10, 11, 7]

# print(quick_sort(test_list))