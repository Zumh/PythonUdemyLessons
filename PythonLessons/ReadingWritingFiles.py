# This will provide python insturction that write to a file
# r for reading
# a for appending

filew = open("C:/Users/ZLConestoga/Desktop/ProjectX/filename.txt", "w")
filew.write("Sample text")
filew.close ()

filea = open("C:/Users/ZLConestoga/Desktop/ProjectX/filename.txt", "a")
filea.write("Sample text")
filea.close ()
path = "C:/Users/ZLConestoga/Desktop/ProjectX/filename.txt"
days_file = open(path,'r').read()
print(days_file)

