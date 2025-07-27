#A[i]<=A[j] where A[j] is the smallest value
#A[i]>=A[j] where A[j] is the largest value
#t = 1,3,5,7 i.e. t%2 = 1
#t = 0,2,4,6 i.e. t%2 = 0

#count = input("Enter the number of students: ")
#inputarray = input("Enter the array of staudents: ")
#inputarray = inputarray.split()
#numarray = []
count = 1
n = 10
#numarray = [34,67,43,78,89]
#numarray = [25,78,10,10,79]
#numarray = [1,1,1]
numarray = [1,2,3,4,5,6,6,7,8,8]

import sys
 
class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None  #parent node
        self.left = None   # left node
        self.right = None  # right node
        self.color = 1     #1=red , 0 = black
 
 
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
 
    # Preorder
    def pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
 
    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right
 
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
 
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left
 
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
 
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0
 
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
 
    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node
 
            if node.item <= key:
                node = node.right
            else:
                node = node.left
 
        if z == self.TNULL:
            print("Cannot find key in the tree")
            return
 
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
 
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)
 
    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
 
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
 
    # Print
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
 
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)
 
    def preorder(self):
        self.pre_order_helper(self.root)
 
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
 
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node
 
    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)
 
        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y
 
    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)
 
        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent
 
        return y
 
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
 
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
 
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
 
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
 
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
 
        y = None
        x = self.root
 
        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right
 
        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
 
        if node.parent == None:
            node.color = 0
            return
 
        if node.parent.parent == None:
            return
 
        self.fix_insert(node)
 
    def get_root(self):
        return self.root
 
    def delete_node(self, item):
        self.delete_node_helper(self.root, item)
 
    def print_tree(self):
        self.__print_helper(self.root, "", True)

rbtree = RedBlackTree()

for i in range(n):
    t = 1
    index1 = i
    index2 = i + 1
    rbtree.insert(numarray[i])

#for num in inputarray:
#        numarray = numarray + [int(num)]

def sort_array(numarray):
    for i in range(n):
        for j in range(0, n-i-1):
            if numarray[j] > numarray[j+1]:
                numarray[j], numarray[j+1] = numarray[j+1], numarray[j]
    return numarray

sorted_array = sort_array(numarray)

# Example usage:
sorted_arr = sort_array(numarray)
print("Sorted array is:", sorted_arr)


for i in range (0,n):
        t = 1
        index1 = i
        index2 = i + 1
        #print (index1,index2)
        for j in range(i,n-1):
                if (t%2 == 1 and numarray[index1] <= numarray[index2]) or (t%2 == 0 and numarray[index1] >= numarray[index2]):
                    index1 = index2
                    index2 = index2 + 1
                    if (index2 == n):
                           #print (numarray[index1])
                           count = count + 1
                    t = t + 1
                else:
                       #print (numarray[index1])
                       index2 = index2 + 1  
                

print (count)

        