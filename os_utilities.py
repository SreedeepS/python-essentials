import platform
import os
import sys

#os 
print("Process id:", os.getpid())
print("Parent process id:", os.getppid())

#platform
print("Machine network name:", platform.node()) 
print("Python version:", platform.python_version())
print("System: ", platform.system()) #OS name

#sys
print("Python module lookup path:", sys.path)
print("Command to run Python: ", sys.argv)

#Get the username via an environment variable
print("USERNAME environment variable:", os.environ["USERNAME"])