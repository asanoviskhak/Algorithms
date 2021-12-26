# def fact(x):
#   if x==1:
#     return 1
#   else:
#     return x*fact(x-1)

# print(fact(3))

def sum(arr):
  if len(arr)==0:
    return 0
  else:
    return arr.pop()+sum(arr)

print(sum([2,4,6,12,1]))