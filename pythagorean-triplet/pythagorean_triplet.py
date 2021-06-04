
def triplets_with_sum(number):
  return [[a, b, number - a -b] for a in range(number//3) for b in range(a+1,number//2) if a*a + b*b == (number-a-b)*(number-a-b)] 


