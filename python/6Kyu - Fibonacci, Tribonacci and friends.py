# My Solution

def Xbonacci(signature,n):
  res = signature[:n]
  amount = len(signature)
  for i in range(n - amount): res.append(sum(res[-amount:]))
  return res
