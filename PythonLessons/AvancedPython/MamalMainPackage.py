# Import classes from our new package
from Animals import MamalPackage
from Animals import BirdPackage

#Create an object of Mamals class and call a method of it
myMamal = MamalPackage.Mamals()
myMamal.printMember()

# Create an object of Birds class and call a method of it

myBird = BirdPackage.Birds()
myBird.printMembers()

