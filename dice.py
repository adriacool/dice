#Prob(|X1-X2|<=x)
def calc_prob(sides, diff):
  n = sides
  x = diff
  l = [i+1 for i in range(n-x-1)]
  P = (n**2 - 2*sum(l))/n**2
  return P 
#calc_prob(20, 3)
#calc_prob(6, 2)
print("Calculate the probability of some difference between 2 rolls of a fair die with some number of sides:")
print(calc_prob(int(input("How many sides? ")), int(input("Enter difference(inclusive): "))))
