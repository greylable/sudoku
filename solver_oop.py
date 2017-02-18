import dancing_links

class PuzzleData():

    # Initializing the board

    def __init__(self,puzzle):
        self.puzzle = puzzle    # puzzle in str
        self.cell_definition = '012345678'
        self.box_definition = ['012', '345', '678']

    def generate_keys(self,cell_definition,cell_definition1):
    # "Cross product of elements in A and elements in B. 81 items in a list"
        return [a + b for a in cell_definition for b in cell_definition1]

    def generate_keys_all(self):
    # "Cross product of elements in A and elements in B. 81 items in a list"
        return self.generate_keys(self.cell_definition,self.cell_definition)

    def box(self):
    # "Generate box constrains. 9 sublists. Each sublist has 9 items"
        return [self.generate_keys(row_box, row_col) for row_box in self.box_definition for row_col in self.box_definition]

    def column(self):
    # "Generate column constrains. 9 sublists. Each sublist has 9 items"
        return [self.generate_keys(self.cell_definition, c) for c in self.cell_definition]

    def row(self):
    # "Generate row constrains. 9 sublists. Each sublist has 9 items"
        return [self.generate_keys(r, self.cell_definition) for r in self.cell_definition]

    def filter_cell_constrain(self,particular_cell):
        # "Generate constrains for a particular cell. 20 items in a list"
        total_constrain = self.box() + self.column() + self.row()
        container = []
        for sublist in total_constrain:
            if particular_cell in sublist:
                container = container + sublist
        return list(set(container) - set([particular_cell]))

    def dict_puzzle(self):
        # "Making a dictionary to store the key and values of the puzzle"
        trans_puzzle = {}
        key_list = self.generate_keys_all()
        i = 0
        for x in self.puzzle:
            trans_puzzle[key_list[i]] = x
            i = i + 1
        return trans_puzzle

class SparseMatrix():

    def __init__(self,size,choices,puzzle):
        self.puzzle = puzzle
        self.cell_definition = '012345678'
        self.box_definition = ['012', '345', '678']
        #self.number = number
        # size = 2 (4x4) or 3 (9x9)
        self.size = size
        self.choices = choices
        self.mydata = [[0 for x in range((size**4)*4)] for y in range(size**6)]
        self.given_puz = PuzzleData(puzzle).dict_puzzle()

    def get_index(self,cell,number):
        i = int(list(cell)[0])
        j = int(list(cell)[1])
        index = (i*(self.size**2)+j)*(self.size**2) + (number-1)
        return index

    def details(self,cell,number):
        index1 = self.get_index(cell,number)

        space = index1 / (self.size**2)
        row = space / (self.size**2)
        row1 = (self.size**2)*row + (self.size**4) + (number-1)
        col = space % (self.size**2)
        col1 = col*(self.size**2) + (self.size**4)*2 + (number-1)
        box = (row - (row%self.size)) + col/self.size
        box1 = box*(self.size**2) + (self.size**4)*3 + (number-1)
        return [index1,space,row1,col1,box1]

    def get_cell_details(self,cell,number):
        # get index,space,row,col,box for that cell-number (cell 00 number 4)
        # if number == 0: then return all possible number choices for that cell
        if number == 0:
            contain = []
            possible_choice = self.choices

            for i in possible_choice:
                possible_details = self.details(cell,i)
                contain = contain + [possible_details]
            return contain

        else:
            return self.details(cell,number)

    def fill_ones(self,cell,number):
        # return 1 for that cell
        if number == 0:
            for j in self.get_cell_details(cell,number):
                index = j[0]
                space = j[1]
                row = j[2]
                col = j[3]
                box = j[4]
                self.mydata[index][space] = 1
                self.mydata[index][row] = 1
                self.mydata[index][col] = 1
                self.mydata[index][box] = 1
            return self.mydata
        else:
            h = self.get_cell_details(cell,number)
            index = h[0]
            space = h[1]
            row = h[2]
            col = h[3]
            box = h[4]
            self.mydata[index][space] = 1
            self.mydata[index][row] = 1
            self.mydata[index][col] = 1
            self.mydata[index][box] = 1
            return self.mydata

    def get_zeros_dict(self):
        contain = []
        for key in self.given_puz.keys():
            if self.given_puz[key] == str(0):
                contain = contain + [key]
        return contain

    def get_nonzeros_dict(self):
        contain = []
        for key in self.given_puz.keys():
            if self.given_puz[key] != str(0):
                contain = contain + [key]
        return contain

    def iter_fill_ones(self):
        for i in self.get_nonzeros_dict():
            hello = self.fill_ones(i,int(self.given_puz[i]))
        return hello

    def iter_fill_zeros(self,puzzle):
        data = self.iter_fill_ones()

        for i in self.get_zeros_dict():
            b = self.get_cell_details(i,0)
            h = PuzzleData(puzzle).filter_cell_constrain(i)
            contain = []
            for j in h:
                if self.given_puz[j] != '0':
                    get_d = self.get_cell_details(j,int(self.given_puz[j]))
                    contain = contain + [get_d]
            to_del = []
            for c in b:
                for a in contain:
                    for u in range(0,5):
                        if c[u] == a[u]:
                            if c not in to_del:
                                to_del = to_del + [c]
            hello123 = to_del
            not_intersection1 = [x for x in b if x not in hello123]

            for w in not_intersection1:
                index = w[0]
                space = w[1]
                row = w[2]
                col = w[3]
                box = w[4]
                data[index][space] = 1
                data[index][row] = 1
                data[index][col] = 1
                data[index][box] = 1
        return data

class Solver():

    def __init__(self,size,choices,puzzle):
        self.puzzle = puzzle
        self.cell_definition = '012345678'
        self.box_definition = ['012', '345', '678']
        self.size = size
        self.choices = choices
        self.sparsed = SparseMatrix(size,choices,puzzle).iter_fill_zeros(puzzle)


    def solving(self):
        sparse = dancing_links.Matrix(self.sparsed)
        solve_sparse_list = sparse.solve()
        return solve_sparse_list

    def trans_sud(self,puzzle):
        contain = []
        for i in self.solving():
            given_puz = PuzzleData(puzzle).dict_puzzle()
            for j in i:
                number = (j%(self.size**2))+1
                space = j/(self.size**2)
                col = space%(self.size**2)
                row = space/(self.size**2)
                rowcol = str(row)+str(col)
                given_puz[rowcol] = number
            contain = contain + [given_puz]
        return contain

    def trans_str(self,puzzle):
        contain1 = []
        for i in self.trans_sud(puzzle):
            contain = ''
            for key in sorted(i.iterkeys()):
                contain = contain +str(i[key])
            contain1 = contain1 + [contain]
        return contain1


if __name__ == "__main__" :

    #cell_definition = '0123'
    #box_definition = ['01', '23']
    #choices = [1,2,3,4]
    #puzzle = '0030200000030210'


    cell_definition = '012345678'
    box_definition = ['012', '345', '678']
    choices = [1,2,3,4,5,6,7,8,9]
    puzzle = '821746953596813724743259861465987132917325486238461597654138279372594618189672345'


    print Solver(3,choices,puzzle).trans_str(puzzle)
