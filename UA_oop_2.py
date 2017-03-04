import solver_oop
import itertools

from PyQt4 import QtGui
from PyQt4 import QtCore


def trans_dict_to_str(dict_puzz):
    contain1 = []
    for i in dict_puzz:
        contain = ''
        for key in sorted(i.iterkeys()):
            contain = contain +str(i[key])
        contain1 = contain1 + [contain]
    return contain1

def display(translated_puzzle):
    # "Display translated_puzzle into a readable form. May have syntax problem :D"
    total_keys = solver_oop.PuzzleData(puzzle).generate_keys_all()
    contain = ''
    if translated_puzzle == {}:
        #print "Empty puzzle"
        return '{}'
    for i in total_keys:
        contain = contain + format(translated_puzzle[i], '^8') + '|'
        if i[1] == '2' or i[1] == '5':
            contain = contain + '|'
        elif i[1] == '8':
            contain = contain + '|' + '\n'
            if int(i[0]) == 5 or int(i[0]) == 2:
                contain = contain + '\n'
    return contain


class CellProperties():

    def __init__(self,cell,puzzle):
        self.cell = cell
        self.puzzle = puzzle

    def find_row(self):
        contain = []
        row_list = solver_oop.PuzzleData(self.puzzle).row()

        for j in row_list:
            if self.cell in j:
                contain = contain + [str(row_list.index(j)+1)]
        return contain

    def find_col(self):
        contain = []
        col_list = solver_oop.PuzzleData(self.puzzle).column()

        for j in col_list:
            if self.cell in j:
                contain = contain + [str(col_list.index(j)+1)]
        return contain

    def find_box(self):
        contain = []
        box_list = solver_oop.PuzzleData(self.puzzle).box()

        for j in box_list:
            if self.cell in j:
                contain = contain + [str(box_list.index(j)+1)]
        return contain


class UA4():
    def __init__(self,puzzle):
        # puzzle in str
        self.puzzle = puzzle

    def checker(self,removed_cells):
        # check if the removed cells are from same row/col & box
        # If yes, collect the 2 numbers tgt
        contain1 = []
        #if len(removed_cells) > 1:
        for a, b in itertools.combinations(removed_cells, 2):
            if (CellProperties(a,self.puzzle).find_row() == CellProperties(b,self.puzzle).find_row() or CellProperties(a,self.puzzle).find_col() == CellProperties(b,self.puzzle).find_col()) and CellProperties(a,self.puzzle).find_box() == CellProperties(b,self.puzzle).find_box():
                contain1 = contain1 + [[a,b]]
        return contain1

    def find_my_fren(self,x,y):
        # given 2 cells, find the fren that is linked to them.
        row_to_include = list(y[1])[0]
        col_to_include = list(y[1])[1]
        row_me = x[0][0]
        col_me = x[0][1]
        row_me2 = x[1][0]
        col_me2 = x[1][1]
        new_fren = []
        if row_to_include == row_me and row_to_include != row_me2:
            new_fren = x + [y[1]]
        elif col_to_include == col_me and col_to_include != col_me2:
            new_fren = x + [y[1]]
        return new_fren

    def mixing_string(self,str_a,str_b):
        # if str_a = '11', str_b = '10' => Output is ['11', '10']
        left_a = str_a[0]
        right_a = str_a[1]
        left_b = str_b[0]
        right_b = str_b[1]
        concatenate1 = left_a + right_b
        concatenate2 = left_b + right_a
        contain = [concatenate1, concatenate2]
        return contain

    def find_my_last_fren(self,a_sublist):
        # a_sublist = ['00', '
        contain1 = []
        for i in a_sublist:
            contain2 = self.mixing_string(i[1],i[2])
            for j in contain2:
                if j != i[0]:
                    contain3 = [i+[j]]
                    contain1 = contain1 + contain3
        return contain1

    def set_format(self):
        given_puz = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
        contain1 = []
        contain3 = []
        for key in sorted(given_puz.iterkeys()):
            i_frens = solver_oop.PuzzleData(self.puzzle).filter_cell_constrain(key)
            contain = []
            for i in i_frens:
                new_ppl = [key] + [i]
                combi = self.checker(new_ppl)        # check if same box and (row or column)
                contain = contain + combi
            contain1 = contain1 + contain
            #print contain1
            # collection of same box && (row or col) for all of the cells
        #print contain1
            contain2 = []
            for j in i_frens:
                new_ppl2 = [key] + [j]
                for m, n in itertools.combinations(new_ppl2, 2):
                    if (CellProperties(m,self.puzzle).find_row() == CellProperties(n,self.puzzle).find_row() and CellProperties(m,self.puzzle).find_box() != CellProperties(n,self.puzzle).find_box()) or (CellProperties(m,self.puzzle).find_col() == CellProperties(n,self.puzzle).find_col()  and CellProperties(m,self.puzzle).find_box() != CellProperties(n,self.puzzle).find_box()):
                    # same row but not box or same col but not box
                        contain2 = contain2 + [[m,n]]
            contain3 = contain3 + contain2
            #print contain1
            # collection of same row/col but not box for all of the cells

        contain4 = []
        contain7 = []
        for y in contain3:
            for x in contain1:
                if y[0] in x and self.find_my_fren(x,y) != (None or []):          # PROBLEM!!!!!!!!!!! my ['16', '17', is missing #
                    contain4 = contain4 +[self.find_my_fren(x,y)]


        contain5 = self.find_my_last_fren(contain4)
        contain6 = []
        for i in contain5:
              contain6 = contain6 + [sorted(i)]
        new_list_unique = [list(i) for i in set((map(tuple, contain6)))]
        return new_list_unique
    # this function returns the standard format of UA_4 to delete in any puzzle size
    # UA_4 has 16 UA_4 sets (for 4x4 puz) ~ this is correct.
    # UA_4 has 438 UA_4 sets (for 9x9 puz) ~ check w ian.

    def check_element2(self):
        given_puz = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
        contain = []
        for i in self.set_format():
            contain1 = []
            for j in i:
                contain1 = contain1 + [given_puz[j]]
            h = set(contain1)
            if len(h) == 2:
                contain = contain + [i]
        return contain
    # this functions returns the specific format for a given puzzle
    # number of check_element2 < set_format
    # returns a list of sublist. sublist has 4 items inside.

    def deleting_UA(self):

        contain = []
        for i in self.check_element2():
            given_puz = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
            if i != []:
                for j in i:
                    given_puz[j] = '0'
                contain = contain + [given_puz]
        return contain

    #print deleting_UA(b_list,puzzle, cell_definition,box_definition)
    # deletes the selected cells in check_element2
    # returns a list of dict_puz


class BandStackGenerate():

    def __init__(self,puzzle,size):
        self.puzzle = puzzle
        self.size = size

    def band(self):
        rows = solver_oop.PuzzleData(self.puzzle).row()
        h = self.size
        j = 0
        contain1 = []
        for a in range(9):
            while h <= self.size**2:
                contain = [i for i in rows[j:h]]
                concat_list = [b for c in contain for b in c]
                h = h + self.size
                j = j + self.size
                contain1 = contain1 + [concat_list]
        return contain1

    def stack(self):
        columns = solver_oop.PuzzleData(self.puzzle).column()
        h = self.size
        j = 0
        contain1 = []
        for a in range(9):
            while h <= self.size**2:
                contain = [i for i in columns[j:h]]
                concat_list = [b for c in contain for b in c]
                h = h + self.size
                j = j + self.size
                contain1 = contain1 + [concat_list]
        return contain1

    def band_stack_combi(self,band_no,stack_no):
        if band_no == 0:
            # i.e take all stacks and combi it.
            contain_stack_pure = []
            for x in itertools.combinations(self.stack(),stack_no):
                contain_stack_pure = contain_stack_pure + list(x)
            return contain_stack_pure
        elif stack_no == 0:
            # i.e take all stacks and combi it.
            contain_band_pure = []
            for x in itertools.combinations(self.band(),band_no):
                contain_band_pure = contain_band_pure + list(x)
            return contain_band_pure
        elif band_no == 1 and stack_no == 1:
            all_grids = [self.band()] + [self.stack()]
            contain_mix_1_1 = []
            for h in itertools.product(*list(all_grids)):
                contain_mix = []
                for j in list(h):
                    contain_mix = contain_mix + j
                contain_mix_1_1 = contain_mix_1_1 + [contain_mix]
            return contain_mix_1_1


class BandStackCombi():

    def __init__(self,puzzle,size):
        self.puzzle = puzzle
        self.choices = [1,2,3,4,5,6,7,8,9]
        self.size = size

    def select_a_digit(self,digit,band_stack):
        data_puz = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
        #contain1 = []
        #for i in band_stack:
        contain = []
        for j in band_stack:
            if data_puz[j] == str(digit):
                contain = contain + [j]
        return sorted(list(set(contain)))

    def iterate_numbers_tuple(self,band_stack,tuple_seq):
        # eg. digit 6, has 3 cells in a band. so, this function returns a list of 3 items inside
        contain = []
        for i in self.choices:
            contain1 = self.select_a_digit(i,band_stack)
            contain = contain + [contain1]
        contain3 = []
        for x in contain:
            contain2 = []
            for j in itertools.combinations(x,tuple_seq):
                contain2 = contain2 + [list(j)]
            contain3 = contain3 + [contain2]
        return contain3

    def check_origins(self,band_stack):
        band_stack_first = band_stack[:27]
        band_stack_second = band_stack[27:]
        band_stack_first_band = BandStackGenerate(self.puzzle,self.size).band_stack_combi(1,0)
        band_stack_first_stack = BandStackGenerate(self.puzzle,self.size).band_stack_combi(0,1)
        #return band_stack_first_band
        index_band_stack_first = band_stack_first_band.index(band_stack_first)
        index_band_stack_second = band_stack_first_stack.index(band_stack_second)
        return [index_band_stack_first,index_band_stack_second]

    def check_linkages(self,cell):
        band_original = BandStackGenerate(self.puzzle,self.size).band()
        stack_original = BandStackGenerate(self.puzzle,self.size).stack()
        for i in band_original:
            if cell in i:
                contain1 = band_original.index(i)
                #break
        for j in stack_original:
            if cell in j:
                contain = stack_original.index(j)
        return [contain1, contain]

    def find_linkages(self,a_list):
        contain = []
        for x,y in itertools.combinations(a_list,2):
            if self.check_linkages(x)[0] == self.check_linkages(y)[0] or self.check_linkages(x)[1] == self.check_linkages(y)[1]:
                contain = contain + ['Same Stack/Band']
        return contain

    def iterate_numbers_tuple_mix(self,band_stack,tuple_seq):
        check_origins_list = self.check_origins(band_stack)
        a = check_origins_list[0]
        b = check_origins_list[1]
        band_stack1 = BandStackGenerate(self.puzzle,self.size).band_stack_combi(1,0)[a]
        band_stack2 = BandStackGenerate(self.puzzle,self.size).band_stack_combi(0,1)[b]
        band_stack_iterate1 = self.iterate_numbers_tuple(band_stack1,tuple_seq)

        band_stack_iterate2 = self.iterate_numbers_tuple(band_stack2,tuple_seq)
        back_stack_iterate_1_and_2 = band_stack_iterate1 + band_stack_iterate2
        contain = []
        for i in self.choices:
            contain1 = self.select_a_digit(i,band_stack)
            contain = contain + [contain1]
        contain3 = []
        for x in contain:
            contain2 = []
            for j in itertools.combinations(x,tuple_seq):
                if [list(j)] not in back_stack_iterate_1_and_2:
                    if tuple_seq != 2:
                        if len(self.find_linkages(list(j))) > 1:
                            contain2 = contain2 + [list(j)]
                    else:
                        contain2 = contain2 + [list(j)]
            contain3 = contain3 + [contain2]
        return contain3

    def combi_across_all_digit(self,band_stack,tuple_seq,tuple_set_no):
        combi_list = self.iterate_numbers_tuple(band_stack,tuple_seq)
        #triplet_no = 2 means got 2 sets of triplets
        contain2 = []
        for x in itertools.combinations(combi_list,tuple_set_no):
            contain1 = []
            for h in itertools.product(*list(x)):
                contain = []
                for j in h:
                    contain = contain + j
                contain1 = contain1 + [sorted(contain)]
            contain2 = contain2 + contain1
        return contain2

    def combi_across_all_digit_mix(self,band_stack,tuple_seq,tuple_set_no):
        combi_list = self.iterate_numbers_tuple_mix(band_stack,tuple_seq)
        #triplet_no = 2 means got 2 sets of triplets
        contain2 = []
        for x in itertools.combinations(combi_list,tuple_set_no):
            contain1 = []
            for h in itertools.product(*list(x)):
                contain = []
                for j in h:
                    contain = contain + j
                contain1 = contain1 + [sorted(contain)]
            contain2 = contain2 + contain1
        return contain2


class BandStackPure():
    #progress_bar_update = QtCore.pyqtSignal()
    def __init__(self,puzzle,size):
        self.puzzle = puzzle
        self.choices = [1,2,3,4,5,6,7,8,9]
        self.size = size

    def band_stack_pure(self):
        tuple_seq_all = [[[2,3]],[[3,2]]]
        band_stack_all = BandStackGenerate(puzzle,3).band_stack_combi(1,0) + BandStackGenerate(puzzle,3).band_stack_combi(0,1)
        contain2 = []
        for h in band_stack_all:
            contain1 = []
            for i in tuple_seq_all:
                contain = []
                for j in i:
                    tuple_seq = j[0]
                    tuple_set_no = j[1]
                    contain = contain + BandStackCombi(self.puzzle,self.size).combi_across_all_digit(h,tuple_seq,tuple_set_no)
                contain1 = contain1 + contain
            contain2 = contain2 + contain1
        return contain2

    def sieve_out_one_tuple(self,band_stack,tuple_seq,tuple_set_no):

        magical_one_tuple = BandStackCombi(self.puzzle,self.size).combi_across_all_digit(band_stack,tuple_seq,tuple_set_no)
        UA_4_list = UA4(self.puzzle).check_element2() # each sublist got 4 items
        contain1 = []
        for h in magical_one_tuple:
            #ensure that each box has at least got 2 cells
            contain_box = []
            contain_row = []
            contain_col = []
            for a in h:
                contain_box = contain_box + CellProperties(a,self.puzzle).find_box()
                contain_row = contain_row + CellProperties(a,self.puzzle).find_row()
                contain_col = contain_col + CellProperties(a,self.puzzle).find_col()
            contain_box2 = []
            contain_row2 = []
            contain_col2 = []
            for b in contain_box:
                contain_box2 = contain_box2 + [contain_box.count(b)]
            for c in contain_row:
                contain_row2 = contain_row2 + [contain_row.count(c)]
            for d in contain_col:
                contain_col2 = contain_col2 + [contain_col.count(d)]
            if (1 not in contain_box2) and (1 not in contain_row2) and (1 not in contain_col2):
                contain1 = contain1 + [h]
        contain2 = []
        for j in contain1:
            if j not in UA_4_list:
                contain2 = contain2 + [j]
        return contain2
    # return list of sublist of the cells to be deleted

    def iterate_sieve_out_band_stack_pure(self):
        tuple_seq_all = [[[2,3]],[[3,2]]]
        #tuple_seq_all = [[[2,4]]]
        band_stack_all = BandStackGenerate(self.puzzle,3).band_stack_combi(1,0) + BandStackGenerate(self.puzzle,3).band_stack_combi(0,1)
        contain2 = []
        for h in band_stack_all:
            contain1 = []
            for i in tuple_seq_all:
                contain = []
                for j in i:
                    tuple_seq = j[0]
                    tuple_set_no = j[1]
                    contain = contain + self.sieve_out_one_tuple(h,tuple_seq,tuple_set_no)
                contain1 = contain1 + contain
            contain2 = contain2 + contain1
        return contain2

    def finding_UA_band_stack_pure(self):

        contain2 = []
        for i in self.iterate_sieve_out_band_stack_pure():
            given_puz_hehe = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
            for j in i:
                given_puz_hehe[j] = '0'
            contain = [given_puz_hehe]
            puzzle_str = trans_dict_to_str(contain)[0]
            contain1 = solver_oop.Solver(3,self.choices,puzzle_str).trans_str(puzzle_str)
            if len(contain1) > 1:
                contain2 = contain2 + [i]
            #progress = self.iterate_sieve_out_band_stack_pure().index(i)+1/len(self.iterate_sieve_out_band_stack_pure())
            #self.progress_bar_update.emit(progress)
        return contain2


class BandStackMix():

    def __init__(self,UA_size,puzzle,size):
        self.UA_size = UA_size
        self.size = size
        self.puzzle = puzzle
        self.choices = [1,2,3,4,5,6,7,8,9]

    def check_if_same_box_and_row_or_col(self,cell_a,cell_b):
        cell_a_box = CellProperties(cell_a,self.puzzle).find_box()
        cell_b_box = CellProperties(cell_b,self.puzzle).find_box()
        cell_a_row = CellProperties(cell_a,self.puzzle).find_row()
        cell_b_row = CellProperties(cell_b,self.puzzle).find_row()
        cell_a_col = CellProperties(cell_a,self.puzzle).find_col()
        cell_b_col = CellProperties(cell_b,self.puzzle).find_col()
        if cell_a_box == cell_b_box:
            if cell_a_row == cell_b_row or cell_a_col == cell_b_col:
                return 'Same Box Same Row/Col'
            else:
                return 'Same Box Diff Row/Col'
        else:
            return 'Different Box'

    def check_box(self,list_a):
        # Check at least 2 boxes in the selected cells, have at least 2 elements in the same row/co
        list_a_combi = itertools.combinations(list_a,2)
        contain = []
        for i in list_a_combi:
            cell_a = i[0]
            cell_b = i[1]
            contain = contain + [self.check_if_same_box_and_row_or_col(cell_a,cell_b)]
        if contain.count('Same Box Same Row/Col') > 2:
            return True

    def sieve_out_band_stack_mixed(self,band_stack,tuple_seq,tuple_set_no):
        #full_band_stack_pure_cells = BandStackPure(self.puzzle,self.size).finding_UA_band_stack_pure()
        magical_one_tuple = BandStackCombi(self.puzzle,self.size).combi_across_all_digit_mix(band_stack,tuple_seq,tuple_set_no)
        #print magical_one_tuple
        #print len(magical_exclude)
        #UA_4_list = UA4(self.puzzle).check_element2() # each sublist got 4 items
        contain1 = []
        for h in magical_one_tuple:
            #ensure that each box has at least got 2 cells
            contain_box = []
            contain_row = []
            contain_col = []
            for a in h:
                contain_box = contain_box + CellProperties(a,self.puzzle).find_box()
                contain_row = contain_row + CellProperties(a,self.puzzle).find_row()
                contain_col = contain_col + CellProperties(a,self.puzzle).find_col()
            contain_box2 = []
            contain_row2 = []
            contain_col2 = []
            for b in contain_box:
                contain_box2 = contain_box2 + [contain_box.count(b)]
            for c in contain_row:
                contain_row2 = contain_row2 + [contain_row.count(c)]
            for d in contain_col:
                contain_col2 = contain_col2 + [contain_col.count(d)]
            if (1 not in contain_box2) and (1 not in contain_row2) and (1 not in contain_col2):
                # need another for at least 2 boxes, got at least 2 numbers in same row/col in that box
                contain1 = contain1 + [h]
        return contain1


        #contain2 = []
        #for j in contain1:
        #    if self.check_box(j) == False:
        #        contain2 = contain2 + [j]
        #return contain2

    def iterate_sieve_out_band_stack_mixed(self):

        tuple_seq_all = [[[3,2]]]
        band_stack_all = BandStackGenerate(self.puzzle,3).band_stack_combi(1,1)
        contain2 = []
        for h in band_stack_all:
            contain1 = []
            for i in tuple_seq_all:
                contain = []
                for j in i:
                    tuple_seq = j[0]
                    tuple_set_no = j[1]
                    contain = contain + self.sieve_out_band_stack_mixed(h,tuple_seq,tuple_set_no)
                contain1 = contain1 + contain
            contain2 = contain2 + contain1
        return contain2

    def finding_UA_band_stack_mixed(self):
        contain2 = []
        for i in self.iterate_sieve_out_band_stack_mixed():
            given_puz_hehe = solver_oop.PuzzleData(self.puzzle).dict_puzzle()
            for j in i:
                given_puz_hehe[j] = '0'
            contain = [given_puz_hehe]
            puzzle_str = trans_dict_to_str(contain)[0]
            contain1 = solver_oop.Solver(3,self.choices,puzzle_str).trans_str(puzzle_str)
            if len(contain1) > 1:
                contain2 = contain2 + [i]
        return contain2


class UAGeneral():

    def __init__(self,UA_size,size,puzzle):
        self.UA_size = UA_size
        self.size = size
        self.puzzle = puzzle

    def find_UA_possibility(self):
        triplet = 3
        pair = 2
        quotient_triple = self.UA_size/triplet
        quotient_pair = self.UA_size/pair
        remainder_triplet = self.UA_size%triplet
        remainder_pair = self.UA_size%pair
        if remainder_triplet != 0:
            triplet_set_amount = self.UA_size-remainder_triplet



if __name__ == "__main__" :

    #cell_definition = '0123'
    #box_definition = ['01', '23']
    #choices = [1,2,3,4]

    cell_definition = '012345678'
    box_definition = ['012', '345', '678']
    choices = [1,2,3,4,5,6,7,8,9]

    #puzzle = '192374658574186293836925417987562134423819576651437982768251349345698721219743865'
    puzzle = '821746953596813724743259861465987132917325486238461597654138279372594618189672345'
    #band_stack = BandStackGenerate(puzzle,3).band_stack_combi(1,1)[8]
    #print band_stack

    #print BandStackMix(6,puzzle,3).sieve_out_band_stack_mixed(band_stack,3,2)

    #print BandStackMix(6,puzzle,3).finding_UA_band_stack_mixed()

    #print BandStackMix(6,puzzle,3).iterate_sieve_out_band_stack_mixed()

    #print BandStackMix(6,puzzle,3).finding_UA_band_stack_mixed()


    #print BandStackMix(6,puzzle,3).sieve_out_band_stack_mixed(band_stack,3,2)
    #print len(BandStackMix(6,puzzle,3).finding_UA_band_stack_mixed())

    #print len(BandStackPure(puzzle,3).finding_UA_band_stack_pure())
    #print UA4(puzzle).check_element2()
    print BandStackPure(puzzle,3).finding_UA_band_stack_pure()
