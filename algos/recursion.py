def fact(x):
  if x==1:
    return 1
  else:
    return x*fact(x-1)


# 4.1 код для функции sum
def sum(arr):
  if len(arr)==0:
    return 0
  else:
    return arr.pop()+sum(arr)


# 4.2 Напишите рекурсивную функцию для подсчета элементов в списке.
def lengthOfArr(arr, length):
  if (len(arr)<=0):
    return length
  arr.pop()
  length+=1
  return lengthOfArr(arr, length)


#4.3 Найдите наибольшее число в списке.

def findMax(arr, mx):
  if (len(arr)<=0):
    return mx
  temp = arr.pop()
  if (temp>mx):
    mx = temp
  return findMax(arr, mx)


