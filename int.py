
Class BigInt():
	def __init__(self,int_list,neg = False):
		#where 1523 represented as [3,2,5,1] 
		self.integer = int_list
		self.neg = neg
		self.length = len(int_list)
	
	def createInt(self,num):
		neg = False
		if num != 0:
			sign = num/abs(num)
			if sign == 1:
				neg = False
			else:
				neg = True
		string_num = str(num) #”1234”
		list_str_num = string_num.split() #[‘1’,’2’...]
		int_list = list_str_num.map(int(x)) #[1,2,3,4]
		correct_order = int_list.reversed() #outputs reversed (built in)
		return BigInt(correct_order,neg)
	
	def add(self,int2):
		shorter = min(self.length,int2.len())
		longer = max(self.length,int2.len())
		if self.neg and int2.neg:
			sumNeg = True
		elif  not self.neg and not int2.neg:
			sumNeg = False
		else:
			if self.neg:
returnInt = sub(int2,self)
else:
	returnInt = sub(self,int2)

return returnInt

		if longer == self.length:
			longer = self
		else:
			longer = int2
		
		carry = 0
		intSum = []
		for i in range(shorter):
			value = self.integer[i] + int2.integer[i] + carry
			carry, value = split(value)
			intSum.append(value)
		
		for j in range(shorter,longer)
			value = longer[j] + carry
			carry,value = split(value)
			intSum.append(value)
		
		return BigInt(intSum,neg)

	def len(self):
		return self.length
		
	def split(value):
		if value < 10:
			return (0,value)
		elif(value < 20):
			return (1,value - 10)

	def sub(int1,int2):
		#where int1 > 0 and int2 < 0
		#example [1,5,3,2,4] - [7,8] where larger number is the positive
		#working on the opposite case

		shorter = min(self.length,int2.len())
		longer = max(self.length,int2.len())
		sumInt = []

		if longer == self.length:
			longer = self
		else:
			longer = int2
		
		carry = 0
		for i in range(shorter):
			value = int1.integer[i] - int2.integer[i] - carry
			if value < 0:
				value = 10 + value
				carry = 1
			else:
				carry = 0
			
			sumInt.append(value)
		for j in range(shorter,longer):
			value = longer.integer[j] - carry
			if value < 0:
				value = 10 + value
				carry = 1
			else:
				carry = 0
			sumInt.append(value)
			
	
int1 = [1,5,3,2,4] #42351
int2 = [7,8]		 #87
intSum = []

longer = int1
[8,3,4,2,4] 	#42438
