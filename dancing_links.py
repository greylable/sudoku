#!/usr/bin/env python

"""
Dancing Links | Sam Auciello | March 2011

An implementation of Knuth's dancing links algorith.

The dancing links algorithm solves the exact cover problem.  The exact cover
 problem is, given a matrix of 0s and 1s find all subsets of the rows in the
 matrix such that each column in the matrix contains exactly one 1 within the
 subset.  For example:
    
    Given the matrix:
    
    0 | 1 1 0
    1 | 0 0 1
    2 | 1 0 1
    3 | 0 1 0
    
    the solutions are [0, 1] and [2, 3].

The dancing links algorithm is a brute force algorithm that recursively searches
 for combinations of rows. It does this by representing the matrix as a grid of
 linked nodes.  Each node represents a 1 in the matrix and contains links to its
 neighbors in each of the cardinal directions (wraping around at the edges).
 Additionally there is a head at the top of each column with additional
 information about the current size of the column and a root to the left of the
 head with information about the current size of the matrix:
 
                     |      |      | 
          - root - head - head - head -
                     |      |      |
                 - node - node -   |
                     |      |      |
                     |      |  - node -
                     |      |      |
                 - node ----|--- node -
                     |      |      |
                        - node -
                            |
            
            The above diagram shows the node structure for the matrix in the
             previous example.

Once this structure is built, the algorithm follows the following procedure:

 1. If the matrix is empty, we've found a solution. Record the currently
  selected row subset and return up to the previous recursion depth.
 2. Select the smallest column.
 3. If this column is empty there is no solution to the current matrix. Return
  up to the previous recursion depth.
 4. Select a row containing a node in this column.
 5. Reduce the matrix by temporarily removing each this row and each row
  containing a node that shares a column with a node in this row. (The algorithm
  is checking for solutions containing this row so it needs to eliminate any
  rows with 1s in the same places).
 6. Recursively run this procedure on the reduced matrix.
 7. Undo the reduction operation.
 8. If there are rows in this column that haven't yet been selected return to
  step 4.

Jim Mahoney's dancing links implementation in C was used heavily for reference.

"""

# Constants #

DEBUG = False
VERBOSE = False
COUNTER = False

# Classes #

class Root() :
    """
    A root node wich keeps track of all heads.
    """
    def __init__(self, children=None) :
        self.col = "Root"
        self.left = self
        self.right = self
        self.count = 0
        if COUNTER : self.counter = 0 # A counter to track the number of
                                            # show/hide operations
        if children == None : # The children list is for matrix building and
            self.children = [] # debugging purposes
        else :                      # It is not used by the search algorithm
            self.children = children

    def __repr__(self) :
        """
        A text representation of the root for debugging purposes.
        """
        out = "root"
        for head in self.children :
            out += "\n - " + str(head)
        return out
    def __setitem__(self, index, value) :
        """
        Allow values of the children list to be set via self[index] = value
        """
        try : self.children[index] = value
        except : pass
    def __getitem__(self, index) :
        """
        Allow values of the children list to be accessed via self[index]
        """
        try : return self.children[index]
        except : return None
    def __len__(self) :
        """
        Allow the length of the children list to be accessed via len(self)
        """
        return len(self.children)
    def empty(self) :
        """
        Return True if there are currently no heads in unhidden
        """
        return self.count == 0
    def appendHead(self, head) :
        """
        Add a newly created head to this root creating the appropriate links
        """
        if not self[0] : # This is the first head
            self.left = self.right = head
            head.left = head.right = self
        else : # This is not the first head
            self.left = self[-1].right = head
            head.left = self[-1]
            head.right = self
        self.children.append(head)
        self.count += 1
    def smallestHead(self) :
        """
        Return head with smallest number of nodes
        """
        if self.count == 0 : return None
        head = self.right
        smallHead = head
        smallCount = head.count
        while head != self :
            if head.count < smallCount :
                smallCount = head.count
                smallHead = head
            head = head.right
        return smallHead

class Head(Root) :
    """
    A head node wich keeps track of all nodes in a column.
    """
    def __init__(self, l=None, r=None, col=None, root=None, children=None) :
        if DEBUG : self.hidden = False
        self.left = l
        self.right = r
        self.up = self
        self.down = self
        self.col = col
        self.root = root
        self.count = 0
        if children == None : # The children list is for matrix building and
            self.children = [] # debugging purposes
        else :                      # It is not used by the search algorithm
            self.children = children
    def __repr__(self) :
        """
        A text representation of the head for debugging purposes.
        """
        out = "head (%s) (left: %s right: %s)" % (
            str(self.col), str(self.left.col), str(self.right.col)
        )
        return out
    def appendNode(self, node) :
        """
        Add a newly created node to this column creating the appropriate links
        """
        if not self[0] : # This is the first node
            self.down = self.up = node
            node.down = node.up = self
        else : # This is not the first node
            self.up = self[-1].down = node
            node.up = self[-1]
            node.down = self
        self.children.append(node)
        self.count += 1
    def hideLeftRight(self) :
        """
        Hide this head from its neighbors to the left and right
        """
        #if COUNTER : self.root.counter += 1
        if DEBUG : self.hidden = True
        self.left.right = self.right
        self.right.left = self.left
        self.root.count -= 1
    def hideUpDown(self) :
        """
        Hide this head from its neighbors above and below
        """
        #if COUNTER : self.root.counter += 1
        if DEBUG : self.hidden = True
        self.up.down = self.down
        self.down.up = self.up
    def hideRowUpDown(self) :
        """
        This method is called for simplicity by the reduce method of a node but
         does nothing
        """
        pass
    def showLeftRight(self) :
        """
        Show this head to its neighbors to the left and right
        """
        #if COUNTER : self.root.counter += 1
        if DEBUG : self.hidden = False
        self.left.right = self.right.left = self
        self.root.count += 1
    def showUpDown(self) :
        """
        Show this head to its neighbors above and below
        """
        #if COUNTER : self.root.counter += 1
        if DEBUG : self.hidden = False
        self.up.down = self.down.up = self
    def showRowUpDown(self) :
        """
        This method is called for simplicity by the replace method of a node but
         does nothing
        """
        pass

class Node() :
    """
    A single node representing a "1" in the matrix connected to the first "1" it
     sees to above below and to eather side of it.
    """
    def __init__(self, l=None, r=None, u=None, d=None, row=None, col=None,
                 head=None) :
        if DEBUG : self.hidden = False
        self.left = l
        self.right = r
        self.up = u
        self.down = d
        self.row = row
        self.col = col
        self.head = head
    def __repr__(self) :
        """
        A text representation of the node for debugging purposes.
        """
        out = "node (%s, %s)\n" % (str(self.row), str(self.col))
        out += "     - left: (%i, %i)\n" % (self.left.row, self.left.col)
        out += "     - right: (%i, %i)\n" % (self.right.row, self.right.col)
        out += "     - up: (%i, %i)\n" % (self.up.row, self.up.col)
        out += "     - down: (%i, %i)\n" % (self.down.row, self.down.col)
        return out
    def reduce(self) :
        """
        Remove this node's row from the matrix
        Remove all other rows that have a 1 in a column that this row has a 1 in
        """
        self.head.hideLeftRight() # Hide this column
        colNode = self.right
        while colNode != self : # Iterate through columns with 1s in this row
            rowNode = colNode.up
            while rowNode != colNode : # Iterate through rows with 1s in this
                rowNode.hideRowUpDown()                     # column
                rowNode = rowNode.up # Hide this row up and down
            colNode = colNode.right
        rowNode = self.up
        while rowNode != self : # Iterate through 1s in this column
            rowNode.hideRowUpDown() # Hide this row up and down
            rowNode = rowNode.up
        colNode = self.right
        while colNode != self : # Iterate through columns with 1s in this row
            rowNode = colNode.up
            while rowNode != colNode : # Iterate through rows with 1s in this
                rowNode.hideLeftRight()                     # column
                rowNode = rowNode.up # Hide this node
            colNode = colNode.right
    def hideLeftRight(self) :
        """
        Hide this node from its neighbors to the left and right
        """
        #if COUNTER : self.head.root.counter += 1
        if DEBUG : self.hidden = True
        self.left.right = self.right
        self.right.left = self.left
    def hideUpDown(self) :
        """
        Hide this node from its neighbors above and below
        """
        #if COUNTER : self.head.root.counter += 1
        if DEBUG : self.hidden = True
        self.up.down = self.down
        self.down.up = self.up
        self.head.count -= 1
    def hideRowUpDown(self) :
        """
        Hide each other node in this row from its neighbors above and below
        """
        node = self.right
        while node != self : # Iterate through nodes in this row
            node.hideUpDown()
            node = node.right
    def replace(self) :
        """
        Undo the steps done in self.remove() in reverse order
        """
        colNode = self.left
        while colNode != self : # Iterate through columns with 1s in this row
            rowNode = colNode.down
            while rowNode != colNode : # Iterate through rows with 1s in this
                rowNode.showLeftRight()                     # column
                rowNode = rowNode.down # Show this node
            colNode = colNode.left
        rowNode = self.down
        while rowNode != self : # Iterate through 1s in this column
            rowNode.showRowUpDown() # Show this row up and down
            rowNode = rowNode.down
        colNode = self.left
        while colNode != self : # Iterate through columns with 1s in this row
            rowNode = colNode.down
            while rowNode != colNode : # Iterate through rows with 1s in this
                rowNode.showRowUpDown()                     # column
                rowNode = rowNode.down # Show this row up and down
            colNode = colNode.left
        self.head.showLeftRight() # Show this column
    def showLeftRight(self) :
        """
        Show this node to its neighbors to the left and right
        """
        #if COUNTER : self.head.root.counter += 1
        if DEBUG : self.hidden = False
        self.left.right = self.right.left = self
    def showUpDown(self) :
        """
        Show this node to its neighbors above and below
        """
        #if COUNTER : self.head.root.counter += 1
        if DEBUG : self.hidden = False
        self.up.down = self.down.up = self
        self.head.count += 1
    def showRowUpDown(self) :
        """
        Show each other node in this row to its neighbors above and below
        """
        node = self.left
        while node != self : # Iterate through nodes in this row
            node.showUpDown()
            node = node.left

class Matrix() :
    """
    A matrix represented using nodes as "1"s
    """
    def __init__(self, array) :
        """
        Build the matrix from an array.
        """
        if VERBOSE : print "Building matrix..."
        if DEBUG :
            self.height = len(array)
            self.width = len(array[0])
        self.solutions = [] # A record of exact-cover solutions
        self.removedRows = [] # Rows in the solution currently being searched
        self.root = Root() # The root of the matrix
        if VERBOSE : print "Generating matrix nodes..."
        for col in range(len(array[0])) : # Make a head for each column index
            head = Head(self.root[-1], self.root[0], col, self.root)

                       #(self, l=None, r=None, col=None, root=None, children=None)
            for row in range(len(array)) : # Make a node for each '1' in the
                if array[row][col] == 1 : # column
                    node = Node(row=row, col=col, head=head)
                    head.appendNode(node)
            head.first = head[0]
            self.root.appendHead(head)
        if VERBOSE : print "Linking nodes horizontally..."
        self.root.first = self.root[0]
        for head in self.root.children : # Connect the nodes to their left and
            for node in head.children : # right neighbors
                rowList = array[node.row]
                if str(type(rowList)) == "<type 'instance'>" :
                    rowList = rowList[:] # Optimization for duck-typing:
                    # When the array passed in is not actually an array but an
                    #  object faking the properties of an array to conserve
                    #  memory, it can save a lot of time to grab this list once
                    #  instead of trying to access it over and over.
                    # TODO: change the matrix construction process so this isn't
                    #  necessary and save even more time.
                left_col = self._getLeft(rowList, node.col)
                node.left = self[node.row, left_col]
                right_col = self._getRight(rowList, node.col)
                node.right = self[node.row, right_col]
        if VERBOSE : print "Matrix built"
    def __getitem__(self, (row, col)) :
        """
        Allow the nodes of the matrix to be accessed via self[row, col]
        """
        for node in self.root[col].children :
            if node.row == row :
                return node
        return None
    def __repr__(self) :
        """
        A text representation of the matrix as a grid for debugging purposes
        """
        if not DEBUG : return "Matrix (for more details turn on debug mode)"
        out = "Matrix:\n  "
        for head in range(self.width) : # Print heads
            if self.root[head].hidden :
                out += "X "
            else :
                out += "+ "
        out += "\n"
        for row in range(self.height) : # Print Nodes
            out += "[ "
            for col in range(self.width) :
                node = self[row, col]
                if node == None :
                    out += "0 "
                elif node.hidden :
                    out += "X "
                else :
                    out += "1 "
            out += "]\n"
        return out
    def _getLeft(self, list, index) :
        """
        Find the index of the first 1 in the list to the left of the specified
         index wrapping around until the original index is reached
        """
        search = list[index:] + list[:index]
        search.reverse() # List reordered to be in the order we want to search
        for x in range(len(search)) :
            if search[x] == 1 :
                return (index - 1 - x) % len(list)
        if DEBUG : print "no 1s in this row"
        return None
    def _getRight(self, list, index) :
        """
        Find the index of the first 1 in the list to the left of the specified
         index wrapping around until the original index is reached
        """
        search = list[index+1:] + list[:index+1] # List reordered to be in the
        for x in range(len(search)) :               # order we want to search
            if search[x] == 1 :
                return (index + 1 + x) % len(list)
        if DEBUG : print "no 1s in this row"
        return None
    def solve(self, depth=0) :
        """
        Recursively depth-first search the possible combinations of rows that
         might meet the constraints.
        """
        if VERBOSE and depth == 0 : print "solving..."
        if DEBUG : print "solving " + str(self)
        if DEBUG : print "cols " + str(self.root.count)
        if self.root.empty() : # Empty matrix: solution found
            self.solved() # record it and backtrack
            return self.solutions # necessary for correct behavior when given an
        head = self.root.smallestHead()                         # empty matrix
        if head.empty() : # Empty column: no solution
            if DEBUG : print "no solution (" + str(depth) + ")"
            return # backtrack
        if DEBUG : print head
        node = head.down
        while node != head : # Iterate through nodes in the selected head
            if COUNTER : self.root.counter += 1
            node.reduce() # Remove this row and all rows that conflict with it
            self.removedRows.append(node.row) # Record row choice
            self.solve(depth + 1) # Recurse
            self.removedRows.pop() # Remove tried row choice
            node.replace() # Replace the rows just removed
            node = node.down
        if depth == 0 :
            if VERBOSE : print "all solutions found: " + str(self.solutions)
            if VERBOSE and COUNTER : print "counter: " + str(self.root.counter)
            return self.solutions
    def solved(self) :
        """
        Record the current solution
        """
        if DEBUG or VERBOSE : print "solution found: " + str(self.removedRows)
        self.solutions.append(self.removedRows[:])
        if VERBOSE : self.solutions[-1].sort()

import csv

def get_sparse():
    contain = []
    #with open('/Users/Bread/Desktop/4x4try.csv', 'rb') as csvfile:
    with open('/Users/Bread/Desktop/new4x4.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            test = map(int, row[0].split(','))
            contain = contain + [test]
    return contain



if __name__ == "__main__" :

    '''a = Matrix([
        [1,1,0],
        [0,0,1],
        [1,0,1],
        [0,1,0]
    ])'''

    #b = Matrix(get_sparse)
    #print b.solve()

    '''a = Matrix([
        [1,1,0],
        [0,0,1],
        [1,0,1],
        [0,1,0]
    ])
    print a
    print a.solve()
    print "\n\n"
    a = Matrix([
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1]
    ])
    print a
    print a.solve()'''




