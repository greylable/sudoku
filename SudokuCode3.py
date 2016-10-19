import random

def generate_keys(A, B):
    "Cross product of elements in A and elements in B. 81 items in a list"
    return [a+b for a in A for b in B]

def box(cell_break):
	"Generate box constrains. 9 sublists. Each sublist has 9 items"
	return [generate_keys(row_box,row_col) for row_box in cell_break for row_col in cell_break]

def column(cell):
	"Generate column constrains. 9 sublists. Each sublist has 9 items"
	return [generate_keys(cell,c) for c in cell]


def row(cell):
	"Generate row constrains. 9 sublists. Each sublist has 9 items"
	return [generate_keys(r,cell) for r in cell]

def filter_cell_constrain(particular_cell,cell,cell_break):
	"Generate constrains for a particular cell. 20 items in a list"
	total_constrain = box(cell_break)+column(cell)+row(cell)
	container = []
	for sublist in total_constrain:
		if particular_cell in sublist:
			container = container + sublist
	return list(set(container)-set([particular_cell]))

def dict_puzzle(puzzle,cell):			
	"Making a dictionary to store the key and values of the puzzle"
	trans_puzzle = {}
	key_list = generate_keys(cell,cell)
	i=0
	for x in puzzle:		
		trans_puzzle[key_list[i]] = x
		i = i + 1
	return trans_puzzle

def display(puzzle,cell):
	"Display puzzle into a readable form. May have syntax problem :D"
	total_keys = generate_keys(cell,cell)
	contain = ''
	if puzzle == {}:
		return '{}'
	for i in total_keys:
		contain = contain + format(puzzle[i],'^8') + '|'
		if i[1] == '3' or i[1] == '6':
			contain = contain + '|'
		elif i[1] == '9':
			contain = contain + '|' + '\n'
			if int(i[0]) == 6 or int(i[0]) ==3:
				contain = contain + '\n'
	return contain	

def markup_one(puzzle,particular_cell,cell,cell_break):
	total_constrain = box(cell_break)+column(cell)+row(cell)
	value = puzzle[particular_cell]
	container = []
	if value == str(0) or len(value) > 1:
		for given_key in filter_cell_constrain(particular_cell,cell,cell_break):
			given_value = puzzle[given_key]
			if given_value != str(0):
				container = container + [given_value]
		return ''.join(set('123456789')-set(container))
	else:
		return value

def markup_all(puzzle,cell,cell_break):
	total_constrain = box(cell_break)+column(cell)+row(cell)
	all_keys = generate_keys(cell,cell)
	for akey in all_keys:
	
		avalue = markup_one(puzzle,akey,cell,cell_break)
		puzzle[akey] = avalue
	return puzzle

def purge(puzzle,particular_cell,value,cell,cell_break):
	"Force a number in. Delete the number from all 3 constrains"	
	container = {}
	keys = filter_cell_constrain(particular_cell,cell,cell_break)
	puzzle[particular_cell] = value
	for i in keys:
		if value in puzzle[i]:
			contain = puzzle[i]
			new_contain = contain.replace(value,'')
			puzzle[i] = new_contain
		else:
			continue
	return puzzle

def check_markup(puzzle,cell_break,cell):
	"loop stops when new_puzzle = puzzle_prev"	
	i = 0
	puzzle_prev = {}
	new_puzzle = puzzle
	#new_puzzle = markup_all(new_puzzle,cell,cell_break)
	counter = 0
	while counter == 0:
		new_puzzle = markup_all(new_puzzle,cell,cell_break)	
		if puzzle_prev == new_puzzle:
			counter = 1
			
		puzzle_prev = puzzle.copy()
		i = i + 1
		#print i
		#print display(translated_puzzle)
	#return str(i) + '\n' + display(translated_puzzle)
	return new_puzzle


def get_min_key(puzzle,cell):
	contain = []
	keys = generate_keys(cell,cell)
	for i in keys:
		if len(puzzle[i]) > 1:
			contain = contain + [puzzle[i] + i]
		
	if contain == []:
		minimal_key = '11'
	else:
		minimal_contain = min(contain,key=len)
		minimal_value = minimal_contain[:-2]
		minimal_key = minimal_contain[-2:]
	
	return minimal_key



def pick_one_cell(marked_up_puzzle, particular_cell, cell_definition, box_definition):		# We currently do length 2

	# value = puzzle[particular_cell]
	# min_value_length = len(value)

	# temp_puzzle = puzzle.copy()
	
	# length = [0]

	# previous_choice = particular_cell
	
	# while 0 in length:

	# 	have_zero = False
	# 	has_all_zero = False

	# 	if value == '':
	# 		print 'Has all zero = True'
	# 		#go to previous cell, and repick.
	# 		has_all_zero = True
	
	# 		break		

	# 	random_choice = random.choice(value)

	# 	print 'This is a random: ' + random_choice
	# 	print 'From cell: ' + particular_cell

	# 	value = value.replace(random_choice,"")

	# 	purge(temp_puzzle,particular_cell,random_choice,cell,cell_break)
	# 	check_markup(temp_puzzle,cell,cell_break)
		
	# 	length = [len(s) for s in temp_puzzle.values()]
	# 	if 0 in length:
	# 		temp_puzzle = puzzle.copy()
	# 		have_zero = True

	# 	#if have_zero == False:
	# 		#previous_choice = random_choice

		# return [temp_puzzle,has_all_zero,previous_choice]

	#temp_puzzle = marked_up_puzzle.copy()
	cell_value = marked_up_puzzle[particular_cell]
	total_num_in_cell = len(cell_value)
	counter = 0
	zero_counter = 0
	all_zeros_in_cell = False
	final_markup = {}

	while counter < total_num_in_cell:
		temp_puzzle = marked_up_puzzle.copy()
		final_markup_has_zero = False

		# Select random value from cell
		random_choice = random.choice(cell_value)
		cell_value = cell_value.replace(random_choice,"")
		# Delete all the same value from cells under the row/box/column constraints
		purged_puzzle = purge(temp_puzzle, particular_cell, random_choice, cell_definition, box_definition)

		final_markup = check_markup(purged_puzzle, box_definition, cell_definition)

		# Check if there are any empty cells in final markup
		for cell in final_markup:
			if len(final_markup[cell]) == 0:
				zero_counter = zero_counter + 1
				final_markup_has_zero = True
				break
			else:
				continue

		if zero_counter == total_num_in_cell:
			all_zeros_in_cell = True

		if final_markup_has_zero == False:
			break

		counter = counter + 1

	# [0] = random_choice, [1] = all_zeros_in_cell, [2] = final_marked_up_puzzle
	return [random_choice, all_zeros_in_cell, final_markup]

def all_len_one(puzzle):
	result = True
	for cell in puzzle:
		if len(puzzle[cell]) != 1:
			result = False
		else:
			continue
	return result
		

def backtrack(marked_up_puzzle, cell_definition, box_definition):
	# contain_prev = []
	# keys = generate_keys(cell,cell)
	# len_more_than_1 = True
	# has_all_zero = False
	# previous_choice = ''
	# while len_more_than_1 == True:

	# 	if has_all_zero == True:
	# 		contain_prev.remove(particular_cell)
	# 		particular_cell = contain_prev[-1]
	# 		print display(pickone(puzzle,particular_cell,cell,cell_break)[0],cell)
	# 		print particular_cell
	# 		print 'im stucked'
			

	# 	else:
	# 		length = sum([len(x) for x in puzzle.values()])	
	# 		particular_cell = get_min_key(puzzle,cell)
	# 		contain_prev = contain_prev + [get_min_key(puzzle,cell)]
			
	# 		print contain_prev, particular_cell
	# 		pickone_list = pickone(puzzle,particular_cell,cell,cell_break)
	# 		puzzle = pickone_list[0]
	# 		has_all_zero = pickone_list[1]
	# 		previous_choice = pickone_list[2]

	# 	if length == 81: #or get_min_key == 'empty':
	# 		len_more_than_1 = False		

	##############################################

	previous_choice_list = []
	previous_puzzle_list = []
	while not all_len_one(marked_up_puzzle):
		random_min_key = get_min_key(marked_up_puzzle, cell_definition)
		print 'I am random '+random_min_key+ '\n' +display(marked_up_puzzle,cell_definition)
		results_list = pick_one_cell(marked_up_puzzle, random_min_key, cell_definition, box_definition)
		
		# [0] = random_choice, [1] = all_zeros_in_cell, [2] = final_marked_up_puzzle
		print "all zeros in cell " + str(results_list[1])
		print "random choice: " + results_list[0]
		print "previous list: " + str(previous_choice_list)
		

		if results_list[1] == True:
			# Go back to previous choice
			previous_choice = previous_choice_list.pop()
			previous_puzzle = previous_puzzle_list[-1]
			print previous_choice
			previous_puzzle[random_min_key].replace(previous_choice, "")
			marked_up_puzzle = previous_puzzle

		else:
			previous_choice_list = previous_choice_list + [results_list[0]]

			previous_puzzle_list = previous_puzzle_list + [results_list[2]]
			# Jump to next cell
			marked_up_puzzle = results_list[2]




	return marked_up_puzzle



#you see, in the whole puzzle, who has len(value) > 1. if got len(value) > 1,
#you will find those ppl who has len(value) > 1,
#then u will pick the minimum of these value.


def solve_puzzle(puzzle,cell_break,cell):
	
	translated_puzzle = dict_puzzle(puzzle,cell)
	translated_puzzle_clone =  translated_puzzle.copy()
	#print 'Original Puzzle' +'\n' + display(translated_puzzle,cell)
	#print markup_one(translated_puzzle,'11',total_constrain)
	first_mark_up = markup_all(translated_puzzle,cell,cell_break)
	more_mark_up = check_markup(first_mark_up,cell_break,cell)
	print 'This is FIRST AND MANY ' + '\n' + display(more_mark_up,cell)
	#print display(purge(first_mark_up,'55','2',cell,cell_break),cell)
	#print display(check_markup(first_mark_up,cell_break,cell),cell)
	#hehe = pickone(first_mark_up,get_min_value(first_mark_up,cell),cell,cell_break)
	#hoho = pickone(hehe,get_min_value(hehe,cell),cell,cell_break)
	#haha = pickone(hoho,get_min_value(hoho,cell),cell,cell_break)	
	#print display(pick_one_cell(more_mark_up,get_min_key(more_mark_up,cell),cell,cell_break)[2],cell)
	print 'Backtrack' + '\n' + display(backtrack(more_mark_up,cell,cell_break),cell)
	#print get_min_value(first_mark_up,cell)


def main():
	#puzzle = '003198070890370600007004893030087009079000380508039040726940508905800000380756900' #hard
	#puzzle = '000310085300040000218000037724069318003080040600004700430000271570603000000001060' #easy
	#puzzle = '001900008600085030007060100034090000000504000000010420005070900010840007700009200' #first puzzle from paper
	puzzle = '039500000000800070000010904100400003000000000007000860006708200010090005000001008'  #hardest puzzle

	cell = '123456789'
	cell_break = ['123','456','789']
	choice_avail = set('123456789')

	solve_puzzle(puzzle,cell_break,cell)

if __name__ == "__main__":
    main()