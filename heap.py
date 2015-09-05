# help via http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html

class MinHeap(object):
	def __init__(self):
		self.heaplist = [0]
		self.currentSize = 0

	def heapifyUp(self,i):
		while (i/2) > 0:
			if self.heaplist[i] < self.heaplist[i/2]:
				parent_value = self.heaplist[i/2]
				self.heaplist[i/2] = self.heaplist[i]
				self.heaplist[i] = parent_value
			i = i/2

	def insert(self,val):
		self.heaplist.append(val)
		self.currentSize += 1
		self.heapifyUp(self.currentSize)

	def heapifyDown(self,i):
		while (i*2) <= self.currentSize:
			min_child = self.minChild(i)
			if self.heaplist[i] > self.heaplist[min_child]:
				tmp = self.heaplist[i]
				self.heaplist[i] = self.heaplist[min_child]
				self.heaplist[min_child] = tmp
			i = min_child

	def minChild(self,i):
		if i*2 + 1 > self.currentSize:
			return i*2
		else:
			if self.heaplist[i*2] < self.heaplist[i*2+1]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		min_element = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heaplist.pop()
		self.heapifyDown(1)
		return min_element

	def buildHeap(self,unsortedArray):
		i = len(unsortedArray)/2
		self.currentSize = len(unsortedArray)
		self.heaplist = [0] + unsortedArray[:]
		while i > 0 :
			self.heapifyDown(i)
			i -= 1

newHeap = MinHeap()
newHeap.buildHeap([9,8,7,6,5,4,3,2,1])
for i in range(newHeap.currentSize):
	print newHeap.delMin()
