# def solution(A, X, D):
#     distance_to_reach = X - D
#     if X <= D:
#         return 0

#     for i in range(len(A)):
#         leaf = A[i]
#         if leaf >= distance_to_reach:
#             inner_leaf = solution(A[:i],X-leaf,X)
#             if inner_leaf != -1:
#             	return i

#     return -1

def solution(A, X, D):
    distance_to_reach = X - D
    furthest_n_sec = 0
    if distance_to_reach < 0:
    	return 0

    for i in range(len(A)):
    	leaf = A[i]
    	distance = leaf - furthest_n_sec
    	if (distance > 0) and distance <= D:
    		furthest_n_sec = leaf
    	if furthest_n_sec >= distance_to_reach:
    		return i

    for j in range(len(A))[::-1]:
    	leaf = A[j]
    	new_distance = leaf - furthest_n_sec
    	if (new_distance > 0) and new_distance <= D:
    		furthest_n_sec = leaf
    	if furthest_n_sec >= distance_to_reach:
    		return len(A)-1

    return -1

A = [1,6,2,4,1,3]
print solution(A,7,2)