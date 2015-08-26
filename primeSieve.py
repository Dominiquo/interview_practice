# return all prime integers less than or equal to A very quickly

def sieve(A):
    prime_list = []
    for number in range(2,A+1):
        is_prime = True
        for prime in prime_list:
			if prime > math.sqrt(number):
				break
			elif (number % prime) == 0:
			    is_prime = False
			    break
        if is_prime:
            prime_list.append(number)
            
    return prime_list