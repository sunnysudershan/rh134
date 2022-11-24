import sys

if sys.version_info.major == 3 and sys.version_info.minor == 8:
    print("This script was correctly run on Python 3.8")
else:
   print("This script was not run on the correct version of Python")
   print("Expected version of Python is 3.8")
   print("Current version of python is %s.%d" %(sys.version_info.major,sys.version_info.minor))
