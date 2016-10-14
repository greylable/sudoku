# Please input puzzle those shit here #

#puzzle = '003198070890370600007004893030087009079000380508039040726940508905800000380756900' #hard
#puzzle = '000310085300040000218000037724069318003080040600004700430000271570603000000001060' #easy
#puzzle = '049132000081479000327685914096051800075028000038046005853267000712894563964513000'  #hidden pair?
puzzle = '000000002000095400006800000085020941000109738100000256893010000000900004007600300' #hidden single
cell = '123456789'

cell_break = ['123','456','789']

class MainLogic:
	def __init__(self):
		self.puzzle = {}
		self.cell = '123456789'

    


def generate_keys(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


#print generate_keys(cell,cell)

def hello(cell):
	return generate_keys(cell,cell)

hello1 = hello(cell)
#print hello1

def dict_puzzle(puzzle,cell):			
	'Making a dictionary to store the key and values of the puzzle'
	trans_puzzle = {}
	key_list = generate_keys(cell,cell)
	i=0
	for x in puzzle:		
		trans_puzzle[key_list[i]] = x
		i = i + 1
	return trans_puzzle
	

translated_puzzle = dict_puzzle(puzzle,cell)
#print translated_puzzle

def box(cell_break):
	return [generate_keys(row_box,row_col) for row_box in cell_break for row_col in cell_break]


def column(cell):
	return [generate_keys(cell,c) for c in cell]

#print column(cell)

def row(cell):
	return [generate_keys(r,cell) for r in cell]

box_constrain = box(cell_break)
column_constrain = column(cell)
row_constrain = row(cell)

#print box_constrain

def total_constrain(cell_break,cell):
	return box(cell_break)+column(cell)+row(cell)


def display(puzzle):
	contain = ''

	for i in hello1:
		contain = contain + format(puzzle[i],'^8') + '|'
		if i[1] == '3' or i[1] == '6':
			contain = contain + '|'
		elif i[1] == '9':
			contain = contain + '|' + '\n'
			if int(i[0]) == 6 or int(i[0]) ==3:
				contain = contain + '\n'

	return contain	


#print display(translated_puzzle)

def filter_box_constrain(particular_cell):
	container = []
	for sublist in box_constrain:
		if particular_cell in sublist:
			container = container + sublist
	return list(set(container)-set([particular_cell]))

def filter_row_constrain(particular_cell):
	container = []
	for sublist in row_constrain:
		if particular_cell in sublist:
			container = container + sublist
	return list(set(container)-set([particular_cell]))

def filter_column_constrain(particular_cell):
	container = []
	for sublist in column_constrain:
		if particular_cell in sublist:
			container = container + sublist
	return list(set(container)-set([particular_cell]))

def filter_cell_constrain(particular_cell,cell_break,cell):
	container = []
	for sublist in total_constrain(cell_break,cell):
		if particular_cell in sublist:
			container = container + sublist
	return list(set(container)-set([particular_cell]))

#print filter_cell_constrain('11',cell_break,cell)

def markup_all_cell(puzzle,cell_break,cell):

	def markup_one_cell(puzzle,particular_cell,cell_break,cell):
		container = []
		choice_avail = set('123456789')
		value = translated_puzzle[particular_cell] ######
		given_keys = filter_cell_constrain(particular_cell,cell_break,cell)
	
		if value == str(0) or len(value) > 1:
			for given_key in given_keys:
				given_value = translated_puzzle[given_key] ######
				if given_value != str(0):
					container = container + [given_value]
			return ''.join(set('123456789')-set(container))

		else:
			return value

	all_keys = translated_puzzle.keys()
	for akey in all_keys:
		avalue = markup_one_cell(puzzle,akey,cell_break,cell)
		translated_puzzle[akey] = avalue
	return translated_puzzle

mark_up_once = markup_all_cell(puzzle,cell_break,cell)

print display(translated_puzzle)

def purge(puzzle,particular_cell,value,cell_break,cell):
	container = {}
	keys = filter_cell_constrain(particular_cell,cell_break,cell)
	puzzle[particular_cell] = value
	for i in keys:
		if value in puzzle[i]:
			contain = puzzle[i]
			new_contain = contain.replace(value,'')
			puzzle[i] = new_contain
		else:
			continue
	return puzzle

#after_purge = purge(mark_up_once,'55','5',cell_break,cell))

def hidden_single(puzzle,particular_cell):
	container = []
	counter = 0
	if len(puzzle[particular_cell]) > 1:
		box_keys = filter_box_constrain(particular_cell)
		row_keys = filter_row_constrain(particular_cell)
		column_keys = filter_column_constrain(particular_cell)
		for j in puzzle[particular_cell]:
			for h in box_keys:
				if len(puzzle[h]) > 1 and set.intersection(set(j),set(puzzle[h])) == set([]):
					counter = counter + 1
					container = container + [j]
				else:
					continue

			if container.count(j) == counter:
				return purge(puzzle,particular_cell,j,cell_break,cell)
			else:
				return puzzle

#print display(hidden_single(mark_up_once,'55'))
				
def backtrack(puzzle):
	contain = []
	keys = generate_keys(cell,cell)
	for i in keys:
		if len(puzzle[i]) > 1:
			contain = contain + [len(puzzle[i])]
	fake_dict = [i,min(contain)]

	
print backtrack(mark_up_once)


