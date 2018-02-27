
# scrip to count... and sum them as a list

a= range(0,1000,3) #defined as a list
b= range(0,1000,5)
c = set(a) | set(b) #redifined as a set and union
print c
print sum(c)
