
'''
nums = [1,2,3,4,5,6,7,8,9]

myList = []
for n in nums:
    myList.append(n)
print (myList)

myList = [n for n in nums]
print (nums)

'''


class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def setData (self, d):
        self.data = d
        
    def get_data(self):
        return self.data
   
    

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
            
    def remove (self, d):
        this_node = self.root
        prev_node = None
        
        while this_node:

            # if the current node is equal to input data
            if this_node.get_data() == d:

                # check for the prev node
                if prev_node:

                    # If it equal to current node then assign prev node next node with current next node
                    prev_node.set_next(this_node.get_next())
                else:

                    # If current node is not equal to current data then move to next node
                    self.root = this_node.get_next()


                # delete current node
                self.size -= 1
                return True # data removed

            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # If it does not find any data

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()

        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.add(8)
print(myList.remove(12))
print(myList.find(5))


            
                    
