import time

print ('The time is:', time.time())

print ('The time that we can read is :', time.ctime())

later = time.time() + 15
print ( '15 seconds from now :', time.ctime(later))

# This is a new program
import os, sys

#show stats of an existing file

stinfo = os.stat('8ball.py')
print(stinfo)

# Using os.stat to receive atime a nd mtime of the file
print ("access time of 8ball.py: %s" %stinfo.st_atime)
print ("moffied time of 8ball.py: %s" %stinfo.st_mtime)

# Modifying the atime and mtime

os.utime ("8ballk.py", (1330712280, 1330712292))
print ("Done!!")

import time
import os

def show_zone_info()
    print ('\ttznmae:', time.tzname)
    print ('\tZone : %d (%d)' % (time.timezone, (time.tiemzone/3600)))
    print ('tDST :' time.daylight)
    print ('\tTime :', time.ctime())

    print ('Default :')
    show_zone_info()

    import time
    print ('gmtime :', time.gmtime())
    print ('localtime', time.localtime())
    
    
          
