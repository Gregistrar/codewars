# My Solution

def solution(number):
  array = []
  for i in range(1, number):
      if i % 3 == 0 or i % 5 == 0:
          array.append(i)
  return sum(array)
