'''puzzle = {'A_A':'0', 'A_B':'0', 'A_C':'0', 'A_D':'3',
		  'B_A':'0', 'B_B':'3', 'B_C':'4', 'B_D':'0',
		  'C_A':'0', 'C_B':'4', 'C_C':'1', 'C_D':'0',
		  'D_A':'1', 'D_B':'0', 'D_C':'0', 'D_D':'0'}'''

'''box = [['A_A','A_B','B_A','B_B'],
	   ['A_C','A_D','B_C','B_D'],
	   ['C_A','C_B','D_A','D_B'],
	   ['C_C','C_D','D_C','D_D']]'''

puzzle = {'A_A':'0', 'A_B':'0', 'A_C':'1', 'A_D':'9', 'A_E':'0', 'A_F':'0', 'A_G':'0', 'A_H':'0','A_I':'8',
		  'B_A':'6', 'B_B':'0', 'B_C':'0', 'B_D':'0', 'B_E':'8', 'B_F':'5', 'B_G':'0', 'B_H':'3','B_I':'0',
		  'C_A':'0', 'C_B':'0', 'C_C':'7', 'C_D':'0', 'C_E':'6', 'C_F':'0', 'C_G':'1', 'C_H':'0','C_I':'0',
		  'D_A':'0', 'D_B':'3', 'D_C':'4', 'D_D':'0', 'D_E':'9', 'D_F':'0', 'D_G':'0', 'D_H':'0','D_I':'0',
		  'E_A':'0', 'E_B':'0', 'E_C':'0', 'E_D':'5', 'E_E':'0', 'E_F':'4', 'E_G':'0', 'E_H':'0','E_I':'0',
		  'F_A':'0', 'F_B':'0', 'F_C':'0', 'F_D':'0', 'F_E':'1', 'F_F':'0', 'F_G':'4', 'F_H':'2','F_I':'0',
		  'G_A':'0', 'G_B':'0', 'G_C':'5', 'G_D':'0', 'G_E':'7', 'G_F':'0', 'G_G':'9', 'G_H':'0','G_I':'0',
		  'H_A':'0', 'H_B':'1', 'H_C':'0', 'H_D':'8', 'H_E':'4', 'H_F':'0', 'H_G':'0', 'H_H':'0','H_I':'7',
		  'I_A':'7', 'I_B':'0', 'I_C':'0', 'I_D':'0', 'I_E':'0', 'I_F':'9', 'I_G':'2', 'I_H':'0','I_I':'0',
		  }



box = [['A_A','A_B','A_C','B_A','B_B','B_C','C_A','C_B','C_C'],
	   ['A_D','A_E','A_F','B_D','B_E','B_F','C_D','C_E','C_F'],
	   ['A_G','A_H','A_I','B_G','B_H','B_I','C_G','C_H','C_I'],
	   ['D_A','D_B','D_C','E_A','E_B','E_C','F_A','F_B','F_C'],
	   ['D_D','D_E','D_F','E_D','E_E','E_F','F_D','F_E','F_F'],
	   ['D_G','D_H','D_I','E_G','E_H','E_I','F_G','F_H','F_I'],
	   ['G_A','G_B','G_C','H_A','H_B','H_C','I_A','I_B','I_C'],
	   ['G_D','G_E','G_F','H_D','H_E','H_F','I_D','I_E','I_F'],
	   ['G_G','G_H','G_I','H_G','H_H','H_I','I_G','I_H','I_I']]


def obtain_row_column(key):
	row = key.split('_')[0]
	column = key.split('_')[1]
	return [row,column]



def row_constrain(puzzle,key):
	element = obtain_row_column(key)
	columns_avail = ['A','B','C','D','E','F','G','H','I']
	choice_avail = '123456789'
	container = []
	if len(puzzle.get(key)) != 1:
		columns_avail.remove(element[1])
		for i in columns_avail:
			get_rest_element = element[0] + '_' + i
			values_taken = puzzle.get(get_rest_element)
			if len(values_taken) == 1: 	########
				container = container + [values_taken]
		values_taken_all = ''.join(container)
		values_not_taken = ''.join(value for value in puzzle.get(key) if value not in values_taken_all)
		return values_not_taken
	elif puzzle.get(key) == str(0):
		columns_avail.remove(element[1])
		for i in columns_avail:
			get_rest_element = element[0] + '_' + i
			values_taken = puzzle.get(get_rest_element)
			if values_taken != str(0):
				container = container + [values_taken]
		values_taken_all = ''.join(container)
		values_not_taken = ''.join(value for value in choice_avail if value not in values_taken_all)
		return values_not_taken
	else:
		return puzzle.get(key)
	


def column_constrain(puzzle,key):
	element = obtain_row_column(key)
	row_avail = ['A','B','C','D','E','F','G','H','I']
	choice_avail = '123456789'
	container = []
	if len(puzzle.get(key)) != 1:
		row_avail.remove(element[0])
		for i in row_avail:
			get_rest_element = i + '_' + element[1]
			values_taken = puzzle.get(get_rest_element)
			if len(values_taken) == 1:	########
				container = container + [values_taken]
		values_taken_all = ''.join(container)
		values_not_taken = ''.join(value for value in puzzle.get(key) if value not in values_taken_all)
		return values_not_taken
	elif puzzle.get(key) == str(0):
		row_avail.remove(element[0])
		for i in row_avail:
			get_rest_element = i + '_' + element[1]
			values_taken = puzzle.get(get_rest_element)
			if values_taken != str(0):
				container = container + [values_taken]
		values_taken_all = ''.join(container)
		values_not_taken = ''.join(value for value in choice_avail if value not in values_taken_all)
		return values_not_taken
	else:
		return puzzle.get(key)


def choose_box(key,box):
	for box_i in box:
		if key in box_i:
			return box_i
	


def box_constrain(puzzle,key,box):
	element = obtain_row_column(key)
	choice_avail = '123456789'
	container = []
	choose_one_box = choose_box(key,box)
	if len(puzzle.get(key)) != 1:
		choose_one_box_1 = [x for x in choose_one_box if x != key]
		for i in choose_one_box_1:
			values_taken = puzzle.get(i)
			if len(values_taken) == 1:
				container = container + [values_taken]
			values_taken_all = ''.join(container)
			values_not_taken = ''.join(value for value in puzzle.get(key) if value not in values_taken_all)
		return values_not_taken

	elif puzzle.get(key) == str(0):
		choose_one_box_1 = [x for x in choose_one_box if x != key]
		for i in choose_one_box_1:
			values_taken = puzzle.get(i)
			container = container + [values_taken]
			values_taken_all = ''.join(container)
			values_not_taken = ''.join(value for value in choice_avail if value not in values_taken_all)
		return values_not_taken

	else:
		return puzzle.get(key)	



def find_common_value(puzzle,key,box):
	container = []
	check_row = row_constrain(puzzle,key)
	check_column = column_constrain(puzzle,key)
	check_box = box_constrain(puzzle,key,box)
	result = frozenset(check_row)&frozenset(check_column)&frozenset(check_box)
	return ''.join(list(result))
	#return check_box



def combine_constrain(puzzle,box):		# markup of initial puzzle (round 1)
	generate_keys = puzzle.keys()

	puzzle_1 = {}
	#puzzle_2 = {}
	for key in generate_keys:
		puzzle_1[key] = find_common_value(puzzle,key,box)

	return puzzle_1


def combine_markup(puzzle,box):		# after markup, remove those numbers repeated.
	generate_keys = puzzle.keys()	# also ensures those markup w 1 item occupies that particular cell.
	puzzle_2 = {}					# i.e naked single.
	for key in generate_keys:
		value = puzzle.get(key)
		if len(value) != 1:
			result1 = frozenset(find_common_value(puzzle,key,box))#&frozenset(value)
			result2 = ''.join(list(result1))
			puzzle_2[key] = result2

		else:
			puzzle_2[key] = value

	return puzzle_2


def naked_singles(puzzle,row):
	columns_avail = ['A','B','C','D']
	container = []

	for i in columns_avail:
		get_rest_element = row + '_' + i
		if len(puzzle.get(get_rest_element)) >= 2:
			puzzle[get_rest_element] = row_constrain(puzzle,get_rest_element)
		#else:
			#container = container + [puzzle.get(get_rest_element)]
	return puzzle

def hidden_tuple(puzzle,key,box):							#Hidden Single means that for a given digit and house only one cell is left to place that digit. The cell itself has more than one candidate left, the correct digit is thus hidden amongst the rest.
	element = obtain_row_column(key)
	container = []
	columns_avail = ['A','B','C','D','E','F','G','H','I']
	rows_avail = ['A','B','C','D','E','F','G','H','I']
	choose_one_box = choose_box(key,box)
	if len(puzzle.get(key)) != 1:
		columns_avail.remove(element[1])
		rows_avail.remove(element[0])
		get_rest_element_by_column = [i + '_' + element[1] for i in rows_avail]
		new_get_rest_element_by_column = [x for x in get_rest_element_by_column if len(puzzle.get(x))!=1]
		get_rest_element_by_row = [element[0] + '_' + i for i in columns_avail]
		new_get_rest_element_by_row = [x for x in get_rest_element_by_row if len(puzzle.get(x))!=1]
		get_rest_element_by_box = [x for x in choose_one_box if x != key and (x not in get_rest_element_by_column and get_rest_element_by_row)]
		new_get_rest_element_by_box = [x for x in get_rest_element_by_box if len(puzzle.get(x))!=1]
		get_rest_element_all = new_get_rest_element_by_column + new_get_rest_element_by_row + new_get_rest_element_by_box
		
	else:
		return puzzle.get(key)




#print box_constrain(new_puzzle,'A_A',box)
#print column_constrain(new_puzzle,'A_G')
#print row_constrain(new_puzzle,'A_A')



new_puzzle = combine_constrain(puzzle,box)
new_puzzle_1 = combine_markup(new_puzzle,box)

#print new_puzzle_1
print hidden_tuple(new_puzzle_1,'I_E',box)





