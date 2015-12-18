import math 
vec = [1,1,1]
a = 1e-100,1e-110,1e-120
b = 1e-101,1e-111,1e-121
c = 1e-102,1e-112,1e-122

for i in range(3):
	large = min([math.log(a[i]),math.log(b[i]),math.log(c[i])])
	vec[0] *= a[i]*math.exp(abs(large))
	vec[1] *= b[i]*math.exp(abs(large))
	vec[2] *= c[i]*math.exp(abs(large))

def normalize(vector):
	total = sum(vector)
	new = [float(i)/total for i in vector]
	return new 

# print vec
print normalize(vec)