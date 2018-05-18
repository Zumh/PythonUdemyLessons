#class that we will create

class Mamals:
    def __init__(self):
        #create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printMember(self):
        print ('Printing members of the Mamals class')
        for members in self.members:
            print('\t%s' % members)
