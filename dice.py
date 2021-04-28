#Prob(|X1-X2|<=x)
n = 20
x = 3
l = [i+1 for i in range(n-x-1)]
P = (n**2 - 2*sum(l))/n**2
print(P) 
