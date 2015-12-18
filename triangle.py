def solution(A):
    A.sort()

    if len(A) < 3:
    	return -1
    print A
    for i in range(2,len(A)):
    	print i
    	p = A[i-2]
    	q = A[i-1]
    	r = A[i]
    	print q,p,r
    	if isValid(p,q,r):
    		return p+q+r
    return -1


def isValid(p,q,r):
	print "checking ",p,q,r
	statement1 = (p+q) > r
	statement2 = (p+r) > q
	statement3 = (r+q) > p
	if statement1 and statement2 and statement3:
		print "checked and tru  ",p,q,r
		return True
	else:
		return False


A = [5, 10, 18, 7, 8, 3]
print solution(A)