# AVLTree.py
# COMP 150
# Created by Cori Jacoby
# 4/24/2017

# AVL tree implementation to be used by optimal construction
# algorithms

from BSTTree import BSTTree

#created a subclass AVL Tree class to add in balancing factor

class AVLTree(BSTTree):

    def __init__(self, value):
        BSTTree.__init__(self, value)
        self.balance = 0
        self.parent = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return self.return_root()
        else:
            if value < self.value:
                # Recursion on child isn't possible unless it's initialized
                if self.left is None:
                    self.left = AVLTree(value)
                    self.left.parent = self
                    return self.rebalance(self.left)
                else:
                    return self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = AVLTree(value)
                    self.right.parent = self
                    return self.rebalance(self.right)
                else:
                    return self.right.insert(value)
            elif value == self.value:
                return self.return_root()

    def rebalance(parent, child):
        grandparent = parent.parent
        sub_root = None
        if parent.left == child:
            if parent.balance < 0:
                if child.balance > 0:
                    sub_root = child.right
                    parent.rotate_leftright(child)
                else:
                    parent.rotate_right(child)
                    sub_root = child
            else:
                if parent.balance > 0:
                    parent.balance = 0
                    return parent.return_root()
                else:
                    parent.balance -= 1
                    if grandparent != None:
                        return grandparent.rebalance(parent)
                    else:
                        return parent
        else:
            if parent.balance > 0:
                if child.balance < 0:
                    sub_root = child.left
                    parent.rotate_rightleft(child)
                else:
                    parent.rotate_left(child)
                    sub_root = child
            else:
                if parent.balance < 0:
                    parent.balance = 0
                    return parent.return_root()
                else:
                    parent.balance += 1
                    if grandparent != None:
                        return grandparent.rebalance(parent)
                    else:
                        return parent

        if grandparent != None:
            if grandparent.left == parent:
                grandparent.left = sub_root
            else:
                grandparent.right = sub_root
        sub_root.parent = grandparent
        
        return sub_root.return_root()


    def rotate_right(self, child):
        self.left = child.right
        if self.left != None:
            self.left.parent = self

        child.right = self
        self.parent = child

        self.balance = 0
        child.balance = 0

        return

    def rotate_left(self, child):
        self.right = child.left
        if self.right != None:
            self.right.parent = self

        child.left = self
        self.parent = child

        self.balance = 0
        child.balance = 0

        return

    def rotate_rightleft(self, child):
        gchild = child.left

        child.left = gchild.right
        if child.left != None:
            child.left.parent = child
        gchild.right = child
        child.parent = gchild

        self.right = gchild.left
        if self.right != None:
            self.right.parent = self
        gchild.left = self
        self.parent = gchild

        if gchild.balance > 0:
            self.balance = -1
            child.balance = 0
        elif gchild.balance == 0:
            self.balance = 0
            child.balance = 0
        else:
            self.balance = 0
            child.balance = 1

        gchild.balance = 0
        return

    def rotate_leftright(self, child):
        gchild = child.right

        child.right = gchild.left
        if child.right != None:
            child.right.parent = child
        gchild.left = child
        child.parent = gchild

        self.left = gchild.right
        if self.left != None:
            self.left.parent = self
        gchild.right = self
        self.parent = gchild

        if gchild.balance > 0:
            self.balance = 0
            child.balance = -1
        elif gchild.balance == 0:
            self.balance = 0
            child.balance = 0
        else:
            self.balance = 1
            child.balance = 0

        gchild.balance = 0
        return

    def return_root(self):
        parent = self.parent
        if parent == None:
            return self
        else:
            return parent.return_root()

def test():
    t = AVLTree(5)
    lt = [1, 7, 10, 9, 8, 4, 2, 3]
    for x in lt:
        t = t.insert(x)

    print t
