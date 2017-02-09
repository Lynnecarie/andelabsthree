class BinarySearch(list):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b    
		for i in range(1,a+1):
			self.append(i*b)

		self.length = len(self)
	def search(self, value):
		self.sort()
		
		left = 0
		right = self.length - 1
		
		count = 0
		while 1:

			middle = ((left + right) // 2) 
			if left > right or middle > right:
				return {'count':count, 'index':-1}
			
			if self[middle] == value:
				return {'count':count, 'index':middle}
			elif self[right] == value:
				return {'count':count, 'index':right}
			elif self[left] == value:
				return {'count':count, 'index':left}
			elif middle==left or middle==right:
				return {'count':count, 'index':-1}			
			elif self[middle] < value:
				left = middle + 1
			elif self[middle] > value:
				right = middle - 1
			count+=1