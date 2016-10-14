class MainLogic:
	def __init__(self):
		self.puzzle = {}
		self.cell = '123456789'
		self.cell_break = ['123', '456', '789']

	def generate_keys(A, B):
		return [a+b for a in A for b in B]


