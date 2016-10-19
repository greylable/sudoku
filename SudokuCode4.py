class PuzzleData:
	
	def __init__(self, puzzle):
		print "initializing puzzledata object"
		self.puzzle = puzzle
		self.translated_puzzle = {}
		self.cell = '123456789'
		self.cell_break = ['123','456','789']
		self.total_keys = []

	def generate_keys(self, cell_a, cell_b):
		print "generating keys"
		self.total_keys = [a+b for a in cell_a for b in cell_b]

	def dict_puzzle(self, puzzle):			
		print "dict"
		trans_puzzle = {}
		self.generate_keys(self.cell, self.cell)
		key_list = self.total_keys
		print "keylist: " + str(key_list)
		i=0
		for x in puzzle:		
			trans_puzzle[key_list[i]] = x
			i = i + 1
		return trans_puzzle

	def translate_puzzle(self):
		print "translating puzzle"
		self.translate_puzzle = self.dict_puzzle(self.puzzle)

	def box(cell_break):
		"Generate box constrains. 9 sublists. Each sublist has 9 items"
		return [generate_keys(row_box,row_col) for row_box in cell_break for row_col in cell_break]

	def column(cell):
		"Generate column constrains. 9 sublists. Each sublist has 9 items"
		return [generate_keys(cell,c) for c in cell]


	def row(cell):
		"Generate row constrains. 9 sublists. Each sublist has 9 items"
		return [generate_keys(r,cell) for r in cell]

	def filter_cell_constrain(particular_cell, total_constrain):
		"Generate constrains for a particular cell. 20 items in a list"
		container = []
		for sublist in total_constrain:
			if particular_cell in sublist:
				container = container + sublist
		return list(set(container)-set([particular_cell]))

	def display(self, puzzle):
		contain = ''
		if puzzle == {}:
			return '{}'
		for i in self.total_keys:
			contain = contain + format(puzzle[i],'^8') + '|'
			if i[1] == '3' or i[1] == '6':
				contain = contain + '|'
			elif i[1] == '9':
				contain = contain + '|' + '\n'
				if int(i[0]) == 6 or int(i[0]) ==3:
					contain = contain + '\n'
		return contain	


def markup_one(puzzle, particular_cell, total_constrain):

	value = puzzle[particular_cell]
	container = []
	if value == str(0) or len(value) > 1:
		for given_key in filter_cell_constrain(particular_cell,total_constrain):
			given_value = puzzle[given_key]
			if given_value != str(0):
				container = container + [given_value]
		return ''.join(set('123456789')-set(container))
	else:
		return value

def markup_all(puzzle, total_keys, total_constrain):
	all_keys = total_keys
	for akey in all_keys:
	
		avalue = markup_one(puzzle,akey,total_constrain)
		puzzle[akey] = avalue
	return puzzle


def solve_puzzle(puzzle, cell_break,cell):
	total_keys = generate_keys(cell,cell)
	total_constrain = box(cell_break)+column(cell)+row(cell)
	#filter_constrain = filter_cell_constrain(particular_cell,total_constrain)
	translated_puzzle = dict_puzzle(puzzle,total_keys)
	translated_puzzle_clone =  translated_puzzle.copy()
	print display(translated_puzzle,total_keys)
	#print markup_one(translated_puzzle,'11',total_constrain)
	print display(markup_all(translated_puzzle, total_keys, total_constrain), total_keys)

def main():
	puzzle = '003198070890370600007004893030087009079000380508039040726940508905800000380756900' #hard
	#puzzle = '000310085300040000218000037724069318003080040600004700430000271570603000000001060' #easy
	
	puzzle_data_object = PuzzleData(puzzle) 	
	puzzle_data_object.translate_puzzle()
	print "puzzle_data's puzzle member: " + puzzle_data_object.puzzle
	print "puzzle_data's translated puzzle member: " + str(puzzle_data_object.translated_puzzle)
	#choice_avail = set('123456789')

	#solve_puzzle(puzzle,cell_break,cell)

if __name__ == "__main__":
    main()